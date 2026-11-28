import unittest

import test_location_highlights as fixtures
from validate import Invalid


class ClientContractTests(unittest.TestCase):
    setUp = fixtures.LocationHighlightTests.setUp
    write = staticmethod(fixtures.LocationHighlightTests.write)
    stage = fixtures.LocationHighlightTests.stage

    def test_identifiers_for_product_matching(self):
        self.item.update(barcode="12345", variant="unsweetened", pack_count=2)
        self.write(self.candidate / "DE.json", self.feed)
        self.assertEqual(self.stage()["countries"][0]["code"], "DE")

    def test_invalid_display_and_match_fields(self):
        for field, value in (("product_name", "x" * 121), ("brand", {}),
                             ("normal_price", "9" * 129), ("logo_url", ""),
                             ("pack_count", True), ("pack_count", 1001)):
            with self.subTest(field=field), self.assertRaises(Invalid):
                self.feed["items"] = [dict(self.item, **{field: value})]
                self.write(self.candidate / "DE.json", self.feed)
                self.stage()
            self.assertFalse((self.candidate / "index.json").exists())

    def test_encoded_bytes_must_match_android_transport(self):
        path = self.candidate / "DE.json"
        original = path.read_text(encoding="utf-8")
        for raw in (original.encode("utf-16"), original.encode("utf-8-sig"),
                    original.encode("utf-8") + b" " * (900 * 1024)):
            path.write_bytes(raw)
            with self.assertRaises(ValueError):
                self.stage()
            self.assertFalse((self.candidate / "index.json").exists())
