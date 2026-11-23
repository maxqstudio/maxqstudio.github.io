# Crawler extraction — natural product names and structured identity

**Mandatory for every product candidate** discovered from a retailer flyer, receipt-style catalog, official online shop, marketplace product page, or other authorized source. This policy applies to both ordinary-price observations (audit only) and genuine discounted Product Highlights. Normalize names **before** identity matching, deduplication, quality review and production candidate generation.

## Principle

Catalog/receipt abbreviations are not suitable as user-facing product names. Expand common abbreviations to **natural, readable full names**, while preserving brand spelling, product variant, unit and package identity. The normalization step must **not** invent missing details or change which physical SKU, flavor, pack quantity, or store offer is represented.

The original raw text and a source pointer/screenshot must remain in **separate audit evidence** for traceability. Normalization is a deterministic cleanup or a source-reviewed extraction, **not** independent product proof.

## Required Indonesian abbreviation expansion (case-insensitive, token/context aware)

| Source abbreviation | Natural normalized text | Notes |
|---|---|---|
| `MYK GRG` | **Minyak Goreng** | Treat as one phrase, not unrelated tokens |
| `KCP MNS` | **Kecap Manis** | Expand only when used as product category |
| `PCH` | **Pouch** | Packaging form; retain if needed to distinguish variants |
| `BTL` | **Botol** | Packaging form |
| `KTG` | **Kaleng** | Packaging form |
| `SBN MND` | **Sabun Mandi** | Product category |
| `DTRGN` | **Deterjen** | Product category |

**Keep established terms unexpanded**: `UHT`, `3in1`, `SPF`, `ml`, `g`, `kg`, `L`, `pcs`. Normalize unit spacing/case for readability, e.g. `2L` → `2 L`, `250ML` → `250 ml`, `800G` → `800 g`. `SPF 50` stays `SPF 50`. Do not interpret unknown abbreviations, branded acronyms or SKU codes by guessing. Use locale-specific dictionaries for other countries only when the expansion is actually verified in that locale.

**Token safety:** Apply expansions to whole tokens or recognized multi-token phrases, not substrings inside a brand or variant (e.g. don't rewrite `PCH` within a longer SKU). Prefer longest recognized phrase first. Preserve model IDs and proper brand capitalizations where source-backed.

## Required intermediate extraction fields (audit/working candidate, camelCase)

Record the following as **separate structured fields** in the extraction result, even when a value is unavailable:

- `productName`: readable user-facing complete product name, for example `Bimoli Minyak Goreng 2 L`. Include brand and sale-relevant quantity, but avoid all-caps shorthand and needless repetition. Preserve flavor/form factor in name when omission would merge different SKUs.
- `brand`: verified manufacturer/product brand (`Bimoli`), **not** automatically the store or marketplace seller.
- `variant`: verified flavor, scent, subtype or packaging form (e.g. `Pouch`, `Original`) **only when useful for SKU distinction**; do not guess.
- `packageSize`: verified unit quantity with natural spacing (`2 L`, `250 ml`, `800 g`). For multi-packs, record **per-unit** size when identifiable.
- `packCount`: verified integer number of units in the pack (`3` for explicit `3 x 200 ml`), otherwise `null`; do not assume 1 or parse a model number as pack count.

`brand`, `variant`, `packageSize`, `packCount` may be `null` in **audit extraction** when the source cannot establish them. If product identity, exact price variant or pack economics cannot be verified, reject from production rather than invent details. Retain the unmodified `rawProductText` plus source and normalization decisions **in audit only**.

### Example audit extraction (not production JSON)

```json
{
  "rawProductText": "BIMOLI MYK GRG PCH 2L",
  "productName": "Bimoli Minyak Goreng 2 L",
  "brand": "Bimoli",
  "variant": "Pouch",
  "packageSize": "2 L",
  "packCount": null
}
```

Other examples:

| Raw catalog text | `productName` | `brand` | `variant` | `packageSize` | `packCount` |
|---|---|---|---|---|---|
| `ABC KCP MNS BTL 600ML` | ABC Kecap Manis 600 ml | ABC | Botol | 600 ml | null |
| `LIFEBUOY SBN MND PCH 450ML` | Lifebuoy Sabun Mandi 450 ml | Lifebuoy | Pouch | 450 ml | null |
| `RINSO DTRGN 800G` | Rinso Deterjen 800 g | Rinso | null | 800 g | null |
| `SUSU UHT 3 x 200ML` | Susu UHT 3 × 200 ml | null | null | 200 ml | 3 |
| `CAT SPF 50 100ML` | Cat SPF 50 100 ml* | null | null | 100 ml | null |

*The last row is a format-preservation example, **not a verified sale item**; do not accept arbitrary or ambiguous product identities without source confirmation.

**Keep essential packaging identification:** if `Pouch` vs `Botol` changes the product/price/SKU, it must be retained as `variant` and/or included in `productName`; the abbreviated word must never silently disappear from the underlying product identity just to shorten the Home card.

## Output mapping to CURRENT production (strict compatibility)

**Important:** Pretio Product Highlights currently uses `pretio.product_highlights.v1` with strict fields. Its supported item fields are `product_name` (required), `brand` (optional) and `package_size` (optional). It **does not support** `productName`, `variant`, `packageSize` or `packCount` as extra JSON keys.

- `productName` → `product_name` after evidence review, with readable text; make name sufficiently specific to avoid matching different SKU variants.
- `brand` → optional `brand` only when verified.
- `packageSize` → optional `package_size` only when verified.
- `variant` / `packCount` → **audit-only separate fields** unless their essential meaning is incorporated into the existing `product_name` or `package_size` **without loss of identity**. Do not add unsupported production keys.
- `rawProductText` and source/extraction evidence → **audit only**, not the live feed.
- Retailer/seller is recorded separately as the existing `retailer` field. Never mistake brand for retailer.
- Official same-SKU normal/promo prices, matching photo, dates, eligible area, `catalog_id`, currency and HTTPS source gates remain mandatory; a clean name does **not** qualify an unverified offer.

If the approved schema cannot faithfully represent the distinct package variant and pack count in existing keys, **HOLD** that candidate and report a schema/Android requirement; never merge distinct products or silently lose a price-relevant unit count.

## Watchlist and user-matching implications

Canonical normalized product names improve matching against user-saved products and the planned Watchlist Layer 1, but **normalization alone is not a match**. Matching should consider brand, model, flavor/variant, unit/size, pack count, country and product identity. Different pack sizes, `Pouch` vs `Botol` when material, and ambiguous brands must never be treated as the same item.

A future **lightweight, on-device** manual-entry normalizer may expand recognized user abbreviations and tolerate common typos for candidate search/matching, but must preserve the user's original input and request confirmation for ambiguous matches. This is **an Android implementation task**, not a crawler-skill change, and must be separately reviewed/tested.

## Auditor acceptance checklist

1. Inspect original source text against the normalized `productName`, `brand`, `variant`, `packageSize`, `packCount` fields and evidence.
2. All seven specified Indonesian catalog shorthand mappings expand correctly; `UHT`, `3in1`, `SPF`, `ml`, `g`, `kg`, `L`, `pcs` are preserved appropriately.
3. Validate token boundaries, brand capitalization, local unit formatting and absence of invented brands/variants/counts.
4. Reject merge of two different product sizes/variants/pack counts, including cross-seller listings. Compare item identity to exact source prices and image.
5. Inspect **production JSON strict allowlist**: only `product_name`, `brand`, `package_size` mapped, no raw/camelCase extraction fields or `variant`/`packCount` leaked.
6. Report PASS / FAIL / NOT VERIFIED with raw-to-normalized examples for each accepted batch; hold publication for unresolved identity ambiguity.
