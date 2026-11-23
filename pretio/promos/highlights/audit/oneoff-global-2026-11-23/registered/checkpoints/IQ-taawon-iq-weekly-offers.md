# Pretio — registered source checkpoint

**OWNER SOURCE EXCLUSION (post-run):** Taawon is excluded from all eligible source/product/catalog evidence for this one-off run, including the later discovery-phase access after the GPTBot restriction became known. Keep both historical receipts and incident notes, and do not reinterpret `SKIPPED_BLOCKED` as a verified source. See `../../source-exclusions.json` and `../../discovery/deviations.md`.

Run ID: `pretio-oneoff-global-20261123T040625Z`  
Work unit: `IQ:taawon-iq-weekly-offers` | manifest position: **37/74** | attempt: **1**  
Country: **IQ** | merchant: **Taawon Hypermarket** | mode: **AUDIT**  
Registered URL: <https://store.taawon.iq/>  
Recorded review time: **2026-11-23T09:42:44Z** (page fetch timestamps are not surfaced by the web connector).  
Base/skill SHA: `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`  
Terminal receipt: **SKIPPED_BLOCKED**

## Source and permission check

- The accepted manifest lists `taawon-iq-weekly-offers`, `source_type: official_retailer`, `coverage_type: national`, `valid_until: null`. Existing record's last verification date is 2026-11-15.
- Public robots URL: <https://store.taawon.iq/robots.txt> returned HTTP 200 on direct GET. The `User-agent: *` group allows `/` and has `Content-Signal: search=yes,ai-train=no,use=reference`; an explicit `User-agent: GPTBot` group says `Disallow: /`. Because this task is an AI source-crawling operation, the explicit disallow is treated as a source block. No bypass or alternate agent user-agent was used.
- The browser connector first reported the robots URL as inaccessible. Before that restriction was discovered, the homepage, shop page and contact page had been opened. On noticing the explicit GPTBot disallow, I stopped inspecting offers and retained no item-level product or price rows. This is recorded for transparent audit.
- The public homepage/contact header/footer showed delivery described for Baghdad. Country-wide delivery/price applicability was therefore not verified. A `Terms`/`Privacy` link was not found in the retained contact-page text; the robots block was already decisive.
- The homepage's general “up to 20% off” promotion statement is not a product/variant price pair and does not qualify as a Product Highlight. No product candidate was accepted or retained.

## Location, currency, expiry, references

- Although the catalog record is marked `national`, its own summary says online delivery currently highlights Baghdad and branch availability may vary. Do not represent a Baghdad offer as countrywide without separate evidence.
- IQD is not present in the current Product Highlights currency mapping. This blocks Product Highlights publication for IQ regardless of the source block.
- No current campaign validity interval was verifiable. Classify the catalog `STALE_UNVERIFIED`; the robots restriction, a null `valid_until`, and the historical verification timestamp do not prove expiry or obsolescence. Do not remove or relink it.
- Scanned all current country highlight feeds for `catalog_id=taawon-iq-weekly-offers`: **0 references**. No catalog removal was proposed, so no FK changes are needed.
- Production catalog, Product Highlights, index, currency, location files and source verification timestamps remain unchanged.

## Decision

**SKIPPED_BLOCKED** — robots explicitly disallows GPTBot for the full site. No current catalog content, exact item prices, image matches or source-backed offer dates were collected. No retry or policy workaround is appropriate in this one-source attempt.

## Compact handoff (≤400 words)

Work unit `IQ:taawon-iq-weekly-offers`, position 37/74; run `pretio-oneoff-global-20261123T040625Z`, scope `ONE_OFF_GLOBAL`, base/skill SHA `73fd02fe14c4935c3a95bca49bba3c1498a9cb54`. Receipt: `SKIPPED_BLOCKED`. The registered URL is `https://store.taawon.iq/`. Direct GET of `https://store.taawon.iq/robots.txt` returned HTTP 200 with wildcard `/` allowed and `Content-Signal: search=yes,ai-train=no,use=reference`, but the explicit `GPTBot` group disallows `/`. Since this is an AI crawler task, stop source inspection; no alternate user-agent or access workaround was used. The homepage/shop/contact pages were opened before robots was successfully read; once the disallow was found, offer review stopped and no product price rows were retained. The public header/footer described delivery to Baghdad, so countrywide online reach was not demonstrated. IQD is unsupported in the current highlight currency map. No eligible price pair, product image, current validity interval or product candidate was verified. All country highlight feeds were checked for this catalog ID: zero references. The catalog is `STALE_UNVERIFIED`, not proven expired or obsolete. No production JSON changed. Next manifest input: `IT:conad-it-volantini`.