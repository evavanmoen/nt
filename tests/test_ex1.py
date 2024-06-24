import unittest
from checkout.checkout import Checkout


class TestCheckout(unittest.TestCase):
    def setUp(self):
        # load pricing rules from a JSON file
        pricing_rules = Checkout.load_rules('../pricing_rules/ex1.json')
        self.checkout = Checkout(pricing_rules)

    def test_single_item(self):
        # scan a single item and verify the total
        self.checkout.scan('TSHIRT')
        self.assertEqual(self.checkout.total(), 20.00)

    def test_multiple_items(self):
        # scan multiple items and verify the total
        self.checkout.scan('VOUCHER')
        self.checkout.scan('TSHIRT')
        self.checkout.scan('PANTS')
        self.assertEqual(self.checkout.total(), 32.50)

    def test_two_for_one(self):
        # scan items with a '2 for 1' offer and verify the total
        self.checkout.scan('VOUCHER')
        self.checkout.scan('TSHIRT')
        self.checkout.scan('VOUCHER')
        self.assertEqual(self.checkout.total(), 25.00)

    def test_bulk(self):
        # scan items with a bulk discount and verify the total
        self.checkout.scan('TSHIRT')
        self.checkout.scan('TSHIRT')
        self.checkout.scan('TSHIRT')
        self.checkout.scan('VOUCHER')
        self.checkout.scan('TSHIRT')
        self.assertEqual(self.checkout.total(), 81.00)

    def test_multiple_discounts(self):
        # scan items with multiple discounts applied and verify the total
        self.checkout.scan('VOUCHER')
        self.checkout.scan('TSHIRT')
        self.checkout.scan('VOUCHER')
        self.checkout.scan('VOUCHER')
        self.checkout.scan('PANTS')
        self.checkout.scan('TSHIRT')
        self.checkout.scan('TSHIRT')
        self.assertEqual(self.checkout.total(), 74.50)


if __name__ == '__main__':
    unittest.main()
