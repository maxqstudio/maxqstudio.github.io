"""Schema-level gates for prospective online-shop and marketplace offers.

These tests validate production compatibility, NOT external seller evidence.
Manual/authorized source verification remains mandatory in the updater skill.
"""
from __future__ import annotations

from datetime import date
import importlib.util
from pathlib import Path
import unittest


MODULE = Path(__file__).with_name("validate.py")
spec = importlib.util.spec_from_file_location("pretio_shop_validate", MODULE)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

REGISTERED_SHOP = {
    "official-shop-id": {
        "id": "official-shop-id",
        "merchant": "Example Verified Store",
        "publisher": "Example Marketplace",
        "url": "https://marketplace.example/store/example-verified",
        "source_type": "official_digital_channel",
        "locations": [{"type": "country", "country_code": "ID"}],
    }
}
OFFER = {
    "id": "id-marketplace-example-verified-sku-123",
    "catalog_id": "official-shop-id",
    "retailer": "Example Verified Store",
    "product_name": "Example Product 500 ml",
    "normal_price": "19900",
    "promo_price": "15900",
    "currency": "IDR",
    "image_url": "https://img.marketplace.example/sku-123.jpg",
    "source_url": "https://marketplace.example/product/sku-123",
    "observed_at": "2026-11-23T03:00:00Z",
}


class OnlineShopContractTests(unittest.TestCase):
    def validate_item(self, changes=None, catalogs=None):
        offer = {**OFFER, **(changes or {})}
        return validator.validate_highlight_item(
            offer, "marketplace.test", "ID", "IDR",
            REGISTERED_SHOP if catalogs is None else catalogs,
            date(2026, 11, 23),
        )

    def test_registered_marketplace_store_with_official_host_is_schema_compatible(self):
        self.assertFalse(self.validate_item())

    def test_google_shopping_discovery_is_not_an_acceptable_source_url(self):
        with self.assertRaisesRegex(validator.Invalid, "not the catalog's official website"):
            self.validate_item({"source_url": "https://www.google.com/search?tbm=shop&q=sku-123"})

    def test_new_unregistered_marketplace_seller_cannot_publish(self):
        with self.assertRaisesRegex(validator.Invalid, "unknown catalog id"):
            self.validate_item({"catalog_id": "unapproved-shop"})

    def test_audit_only_marketplace_metadata_must_not_leak_to_feed(self):
        with self.assertRaisesRegex(validator.Invalid, "unsupported keys"):
            self.validate_item({"seller_id": "shop-456"})

    def test_missing_or_invalid_public_discount_is_rejected(self):
        with self.assertRaisesRegex(validator.Invalid, "not a verified discount"):
            self.validate_item({"normal_price": "15900", "promo_price": "15900"})


if __name__ == "__main__":
    unittest.main()
