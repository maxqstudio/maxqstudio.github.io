# Pretio Location V2 Sources

Generated snapshot date: 2026-09-23

## Geographic source

GeoNames dump files are used as the global source:

- `countryInfo.txt` supplies ISO alpha-2 country/territory codes and English display names.
- `admin1CodesASCII.txt` supplies the source's first-level administrative divisions and GeoNames IDs.
- `cities500.zip` supplies GeoNames feature-class `P` populated-place records. The GeoNames readme describes this extract as places with population above 500 or administrative seats down to PPLA4. It is not a complete official municipality register and does not represent every settlement.

The current country index includes 249 two-letter ISO-code rows from `countryInfo.txt`. GeoNames special/deprecated non-ISO entries `AN`, `CS`, and `XK` are excluded. Countries without a populated-place record remain in the index and have an empty place list when the source has none.

GeoNames data is distributed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution: GeoNames.org. GeoNames aggregates data from many sources and supplies it "as is"; the source does not warrant completeness, accuracy, or timeliness. Pretio therefore describes this v2 city-level content as GeoNames populated places, not a complete municipal gazetteer.

## Pretio legacy supplements

For `ID`, `CL`, `RS`, `US`, `ZA`, `DE`, and `CH`, the generator retains existing v1 province/city records from `pretio/promos/location.json` and adds GeoNames content. Existing province and city identity codes are preserved so current catalog rules and stored locations keep matching. These legacy records are attributed to the accepted Pretio v1 source, not relicensed or represented as GeoNames data. The v1 endpoint itself is not modified by this generated directory.

Where a GeoNames ADM1 record corresponds to an existing catalog-country subdivision, the generator maps it to that existing Pretio code using the explicit crosswalk in `tooling/pretio_location_v2/generate.py`; the GeoNames source ID and source code remain in the generated record. Unmatched source divisions receive a `geonames:<id>` identity. GeoNames populated places are attached only to their source ADM1 when that ADM1 is present; otherwise they remain at country level rather than being assigned to an invented subdivision.

## Reproduction

The generator accepts a local GeoNames snapshot directory containing the files below and the accepted v1 JSON. It produces UTF-8 JSON, computes the exact SHA-256 of every per-country file, and binds each digest in `index.json`.

```powershell
py tooling/pretio_location_v2/generate.py `
  --source-dir <downloaded-geonames-snapshot> `
  --legacy-location pretio/promos/location.json `
  --output-dir pretio/location/v2 `
  --snapshot-date 2026-09-23
```

The official upstream files used for this snapshot and their SHA-256 values:

| File | Official URL | SHA-256 |
| --- | --- | --- |
| `countryInfo.txt` | `https://download.geonames.org/export/dump/countryInfo.txt` | `93bafc525813f22e4711ff9ed6d626343094ce48c26388dc7c49189b3d7d5512` |
| `admin1CodesASCII.txt` | `https://download.geonames.org/export/dump/admin1CodesASCII.txt` | `1da92a6323a5fec3176f3f743bf4cf4040fd56a876da55e46fbca23c863aa60a` |
| `cities500.zip` | `https://download.geonames.org/export/dump/cities500.zip` | `a2c9409cc477fb443286fcf69be49391bca61653f62ea5ef4b4f1b4e4cfea7b8` |
| `readme.txt` | `https://download.geonames.org/export/dump/readme.txt` | `b1957379b6c1242c700c98ac9a8aa0a09f56c3c0a50ee72175527005f48ef2c5` |

## Feed contract

- `index.json` is the lightweight country index. Country files are fetched only when selected.
- Each country file is bound by the index's HTTPS URL, revision, and SHA-256 of exact UTF-8 bytes.
- Division IDs and GeoNames place IDs are source identities; visible labels are not identifiers.
- `root_cities` contains source places with no usable ADM1 association. They are not assigned to a fabricated province.
- A country with no Pretio catalog remains selectable. Catalog coverage and geographic availability are separate authorities.
