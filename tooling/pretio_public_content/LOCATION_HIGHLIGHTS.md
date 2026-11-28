# Location-aware Product Highlights — dormant candidate contract

Owner: maxqstudio/pretio#111. Companion Android reader: maxqstudio/pretio#112.

National coverage is not mandatory. Collect verified offers at their real country,
province, city or multi-area scope. Never widen a store/postcode-only offer to
a whole city. Preserve unrepresentable offers for review, not as expired.

## Versioned staging
- Feed schema `pretio.product_highlights.v2`, version 2: same strict legacy
  item/price/currency/catalog/expiry/image rules, plus required `locations`.
- Each location is a canonical country rule, province rule, city rule (including
  root cities), or a distinct OR rule in the same country. Exact codes and names
  must match the SHA/revision-bound location-v2 country file. Country scope
  cannot be mixed with narrower scopes. No invented geographic identifiers.
- Future index schema `pretio.product_highlights.index.v3`, version 3;
  canonical URLs under `/pretio/promos/highlights/v2/`, distinct from v1.
  Index entries bind exact bytes and feed revisions. Candidate subset allowed;
  an absent country must fail closed in the future client.
- The legacy feed/index and production data are untouched. No automatic v1
  migration or national default for a legacy item. The v2 URL is proposed,
  NOT deployed. Current Android PR is dormant and not release-ready.

## Operator commands
Use a fresh **non-public** staging directory with one verified CC.json per
country. Do not use the live `pretio/` tree. The commands do not crawl, fetch
images, certify source rights, publish, or modify live content.

```sh
python tooling/pretio_public_content/validate_location_highlights.py --candidate /path/to/stage --build-index
python tooling/pretio_public_content/validate_location_highlights.py --candidate /path/to/stage
python -m unittest discover -s tooling/pretio_public_content -p 'test_*.py' -v
```

Build refuses to overwrite an existing index. Expired items fail validation.
Source evidence, image decoding and rights, exact region/participation proof
and review are still mandatory. No synthetic test offers enter public feeds.

## Release gates still open
Android transport/index/cache, selected-location filtering before all consumers,
visible labels, regional identity for watchlist/compare, runtime tests, compatible
publication plan and Owner acceptance. No v2 public content until these pass.
