#!/usr/bin/env python3
"""One-off, Indonesia-only public Catalog Promo smoke crawler.

No recurrence, no GitHub write, no change to production feeds. One bounded
attempt per catalog. Only official HTTPS public pages, with robots and
redirect checks. Generates auditable results/receipts in an output directory.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup
from PIL import Image, UnidentifiedImageError

from manifest import build_manifest, coverage

USER_AGENT = "PretioPublicPromoAudit/0.1 (+https://maxqstudio.dev/pretio/)"
TIMEOUT = (5, 12)
MAX_HTML_BYTES = 1_800_000
MAX_IMAGE_BYTES = 3_000_000
MAX_PRODUCTS_PER_SOURCE = 20
RECEIPT_STATUSES = {
    "UPDATED", "SKIPPED_NO_CHANGE", "SKIPPED_NO_PROMO",
    "SKIPPED_UNAVAILABLE", "SKIPPED_BLOCKED", "SKIPPED_UNVERIFIED",
    "BLOCKED_CURRENCY_METADATA", "FAILED",
}


def stamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def official_host(host: str, expected: str) -> bool:
    a = host.lower().removeprefix("www.")
    b = expected.lower().removeprefix("www.")
    return a == b or a.endswith("." + b)


def url_allowed(url: str, expected_host: str) -> bool:
    u = urlparse(url)
    return bool(u.scheme == "https" and u.hostname and
                official_host(u.hostname, expected_host) and
                not u.username and not u.password and u.port in (None, 443))


def verify_robots(session: requests.Session, url: str, host: str) -> tuple[bool, str]:
    parsed = urlparse(url)
    robots_url = parsed.scheme + "://" + parsed.netloc + "/robots.txt"
    try:
        res = session.get(robots_url, timeout=TIMEOUT, allow_redirects=False)
    except requests.RequestException as exc:
        return False, "robots fetch failed: " + type(exc).__name__
    if res.status_code in (401, 403):
        return False, f"robots HTTP {res.status_code}"
    if res.status_code in (404, 410):
        return True, "robots missing, HTTP 404/410"
    if res.status_code != 200:
        return False, f"robots status HTTP {res.status_code}"
    robots = RobotFileParser()
    robots.parse(res.text[:250000].splitlines())
    if not robots.can_fetch(USER_AGENT, url):
        return False, "robots disallows catalog path"
    return True, "robots allowed"


def fetch_html(session: requests.Session, url: str, allowed_host: str) -> tuple[str | None, str, str]:
    if not url_allowed(url, allowed_host):
        return None, "SKIPPED_BLOCKED", "catalog URL not approved HTTPS host"
    permitted, robots_note = verify_robots(session, url, allowed_host)
    if not permitted:
        return None, "SKIPPED_BLOCKED", robots_note
    try:
        # No redirects to unknown destinations, and no authenticated session.
        res = session.get(url, timeout=TIMEOUT, allow_redirects=False, stream=True)
        if res.status_code in (301, 302, 303, 307, 308):
            target = urljoin(url, res.headers.get("Location", ""))
            if not url_allowed(target, allowed_host):
                return None, "SKIPPED_BLOCKED", "redirect outside approved retailer host"
            permitted, why = verify_robots(session, target, allowed_host)
            if not permitted:
                return None, "SKIPPED_BLOCKED", "redirect target " + why
            res.close()
            res = session.get(target, timeout=TIMEOUT, allow_redirects=False, stream=True)
        if res.status_code in (401, 403, 429):
            return None, "SKIPPED_BLOCKED", f"source HTTP {res.status_code}"
        if res.status_code != 200:
            return None, "SKIPPED_UNAVAILABLE", f"source HTTP {res.status_code}"
        mime = res.headers.get("Content-Type", "").lower()
        if not ("html" in mime or "text/plain" in mime):
            return None, "SKIPPED_UNVERIFIED", f"unsupported source MIME {mime[:60]}"
        data = bytearray()
        for chunk in res.iter_content(65536):
            data.extend(chunk)
            if len(data) > MAX_HTML_BYTES:
                return None, "SKIPPED_UNVERIFIED", "page larger than allowed evidence limit"
        return bytes(data).decode(res.encoding or "utf-8", errors="replace"), "FETCH_OK", robots_note
    except requests.RequestException as exc:
        return None, "SKIPPED_UNAVAILABLE", "source fetch failed: " + type(exc).__name__
    finally:
        if "res" in locals():
            res.close()


def decimal(value) -> Decimal | None:
    if value is None or isinstance(value, bool):
        return None
    v = str(value).strip().replace("Rp", "").replace(" ", "")
    # Structured numbers must be unambiguous: 1.399 or 1,399 is ambiguous.
    if not re.fullmatch(r"\d+(?:\.\d{1,2})?", v):
        return None
    try:
        return Decimal(v)
    except InvalidOperation:
        return None


def walk(obj, limit=12000):
    stack = [obj]
    count = 0
    while stack and count < limit:
        current = stack.pop()
        count += 1
        if isinstance(current, dict):
            yield current
            for child in current.values():
                if isinstance(child, (dict, list)):
                    stack.append(child)
        elif isinstance(current, list):
            stack.extend(current)


def extract_discount(offers: object) -> tuple[Decimal, Decimal] | None:
    """Accept only explicit current price and strikethrough/list/reference price."""
    for offer in ([offers] if isinstance(offers, dict) else offers if isinstance(offers, list) else []):
        if not isinstance(offer, dict):
            continue
        current = decimal(offer.get("price"))
        if current is None:
            continue
        specs = offer.get("priceSpecification") or []
        if isinstance(specs, dict):
            specs = [specs]
        originals = []
        for spec in specs if isinstance(specs, list) else []:
            if not isinstance(spec, dict):
                continue
            kind = str(spec.get("priceType", "")).lower()
            if any(key in kind for key in ("listprice", "strikethroughprice", "regularprice")):
                candidate = decimal(spec.get("price"))
                if candidate is not None and candidate > current:
                    originals.append(candidate)
        if len(set(originals)) == 1:
            return originals[0], current
    return None


def product_data(product: dict, source_url: str, expected_host: str) -> dict | None:
    typ = product.get("@type", "")
    types = typ if isinstance(typ, list) else [typ]
    if "Product" not in types and "https://schema.org/Product" not in types:
        return None
    name = product.get("name")
    if not isinstance(name, str) or not name.strip():
        return None
    discount = extract_discount(product.get("offers", {}))
    if not discount:
        return None
    original, promo = discount
    candidates = product.get("image", [])
    images = [candidates] if isinstance(candidates, (str, dict)) else candidates if isinstance(candidates, list) else []
    image_url = None
    for obj in images:
        candidate = obj if isinstance(obj, str) else obj.get("url") if isinstance(obj, dict) else None
        if isinstance(candidate, str) and candidate.startswith("https://"):
            image_url = candidate
            break
    if not image_url:
        return None
    return {"product_name": name.strip()[:120], "normal_price": str(original),
            "promo_price": str(promo), "image_url": image_url, "source_url": source_url}


def extract_products(html: str, catalog_url: str, expected_host: str) -> list[dict]:
    """Collect JSON-LD products only; never infer original price from percentages."""
    soup = BeautifulSoup(html, "html.parser")
    seen, products = set(), []
    for script in soup.select('script[type="application/ld+json"]'):
        value = script.string or script.get_text()
        if not value or len(value) > 750_000:
            continue
        try:
            data = json.loads(value)
        except (ValueError, TypeError):
            continue
        for obj in walk(data):
            candidate = product_data(obj, catalog_url, expected_host)
            if not candidate:
                continue
            key = (candidate["product_name"].casefold(), candidate["normal_price"], candidate["promo_price"])
            if key not in seen:
                seen.add(key)
                products.append(candidate)
            if len(products) >= MAX_PRODUCTS_PER_SOURCE:
                return products
    return products


def verified_image(session: requests.Session, image_url: str, expected_hosts: set[str]) -> tuple[bool, str]:
    host = urlparse(image_url).hostname or ""
    # Retailer-owned CDN hosts may be distinct; only allow hosts already present
    # in the approved catalog registry or the official source host.
    if not any(url_allowed(image_url, allowed) for allowed in expected_hosts):
        return False, "image host not in approved set"
    try:
        res = session.get(image_url, timeout=TIMEOUT, stream=True, allow_redirects=False)
        try:
            if res.status_code != 200:
                return False, f"image HTTP {res.status_code}"
            if not res.headers.get("Content-Type", "").lower().startswith("image/"):
                return False, "image content-type invalid"
            data = bytearray()
            for chunk in res.iter_content(65536):
                data.extend(chunk)
                if len(data) > MAX_IMAGE_BYTES:
                    return False, "image exceeds size limit"
            with Image.open(io.BytesIO(data)) as image:
                image.verify()
            return True, hashlib.sha256(data).hexdigest()
        finally:
            res.close()
    except (requests.RequestException, UnidentifiedImageError, OSError):
        return False, "image fetch or decode failed"


def scan_one(entry: dict, session: requests.Session, image_hosts: set[str]) -> tuple[dict, list[dict]]:
    catalog_url = entry["url"]
    host = urlparse(catalog_url).hostname or ""
    receipt = {"work_id": entry["work_id"], "retailer": entry["retailer"],
               "catalog_url": catalog_url, "checked_at": stamp(),
               "status": "SKIPPED_UNVERIFIED", "reason": "", "verified_products": 0}
    html, outcome, reason = fetch_html(session, catalog_url, host)
    receipt["reason"] = reason
    if html is None:
        receipt["status"] = outcome
        return receipt, []
    candidates = extract_products(html, catalog_url, host)
    accepted = []
    for product in candidates:
        # URL fallback is the official catalog itself; model output cannot
        # create a new field or provide original price without direct evidence.
        valid, evidence = verified_image(session, product["image_url"], image_hosts | {host})
        if valid:
            accepted.append({**product, "image_revision": evidence})
    receipt["verified_products"] = len(accepted)
    receipt["status"] = "UPDATED" if accepted else "SKIPPED_UNVERIFIED"
    receipt["reason"] = ("JSON-LD price pairs and image verified" if accepted else
                         "No complete, explicit discounted-product price pair plus image found; no product fabricated")
    return receipt, accepted


def write_report(outdir: Path, manifest: list[dict], receipts: list[dict], candidates: list[dict]):
    outdir.mkdir(parents=True, exist_ok=True)
    result = coverage(manifest, receipts)
    report = {"scope": "ONE_OFF:ID", "generated_at": stamp(), "publication": "NONE_READ_ONLY",
              "coverage": result, "receipts": receipts,
              "candidate_count": len(candidates),
              "candidate_fields": ["product_name", "normal_price", "promo_price", "image_url", "source_url", "image_revision"],
              "candidates": candidates}
    (outdir / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (outdir / "receipts.json").write_text(json.dumps([{"work_id": r["work_id"], "status": r["status"]} for r in receipts], indent=2) + "\n", encoding="utf-8")
    lines = ["# Pretio — Indonesia one-off catalog scan", "", f"- Generated: {report['generated_at']}",
             f"- Catalogs attempted: {len(receipts)}/{len(manifest)}",
             f"- Verified discounted candidate observations: {len(candidates)}",
             f"- Cycle: {result['cycle_status']} (pending {result['pending']})",
             "- Production data updated: **NO**", "",
             "## Per-catalog results", "",
             "| Retailer | Result | Verified discount candidates |", "|---|---|---:|"]
    for r in receipts:
        lines.append(f"| {r['retailer'].replace('|', '/')} | {r['status']} | {r['verified_products']} |")
    lines += ["", "The initial smoke crawler reads official public HTML/JSON-LD only. Dynamic storefronts, flyer PDFs and visual leaflet tables may require separately approved adapters/OCR. No evidence means no published discount."]
    (outdir / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--country", choices=["ID"], required=True)
    parser.add_argument("--once", action="store_true", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.once:
        parser.error("--once required; this tool does not support a recurring/global scan")
    catalog = json.loads((args.root / "pretio/promos/catalog_app.json").read_text(encoding="utf-8"))
    manifest = build_manifest(catalog, country=args.country)
    approved_hosts = set(catalog["allowed_hosts"])
    receipts, candidates = [], []
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml;q=0.9"})
    session.auth = None
    for entry in manifest:
        try:
            receipt, found = scan_one(entry, session, approved_hosts)
        except Exception as exc:  # fail one catalog, not the entire run
            receipt = {"work_id": entry["work_id"], "retailer": entry["retailer"],
                       "catalog_url": entry["url"], "checked_at": stamp(),
                       "status": "FAILED", "reason": type(exc).__name__, "verified_products": 0}
            found = []
        receipts.append(receipt)
        for item in found:
            candidates.append({"catalog_id": entry["catalog_id"], "retailer": entry["retailer"], **item})
        print(f"{len(receipts)}/{len(manifest)} {entry['retailer']}: {receipt['status']} ({receipt['verified_products']} candidates)", flush=True)
    session.close()
    report = write_report(args.output, manifest, receipts, candidates)
    print(json.dumps(report, indent=2), flush=True)
    return 0 if report["cycle_status"] == "COMPLETED" else 2


if __name__ == "__main__":
    sys.exit(main())
