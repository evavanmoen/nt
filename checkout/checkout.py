import json


class Checkout:
    def __init__(self, pricing_rules):
        self.items = []
        self.pricing_rules = pricing_rules

    def scan(self, item):
        self.items.append(item)

    def total(self):
        pass

    @staticmethod
    def load_rules(file_path):
        # load rules from the external file
        with open(file_path, 'r') as file:
            dt = json.load(file)

        # creating the pricing rules with the apply discount to depends the type
        pricing_rules = {}
        for item, rules in dt.items():
            if rules['type'] == '2_for_1':
                pricing_rules[item] = {
                    'type': '2_for_1',
                    'price': rules['price'],
                    'apply_discount': Checkout._apply_discount_2_for_1
                }
            elif rules['type'] == 'bulk':
                pricing_rules[item] = {
                    'type': 'bulk',
                    'price': rules['price'],
                    'discount_amount': rules['discount_amount'],
                    'min_items': rules['min_items'],
                    'apply_discount': Checkout._apply_discount_bulk
                }
            else:
                pricing_rules[item] = {
                    'type': 'none',
                    'price': rules['price']
                }
        return pricing_rules

    @staticmethod
    def _apply_discount_2_for_1(price, count):
        return (count / 2 + count % 2) * price

    @staticmethod
    def _apply_discount_bulk(min_items, discount_amount, price, count):
        if count >= min_items:
            return count * (price - discount_amount)
        else:
            return count * price

