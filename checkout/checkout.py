import json


class Checkout:
    def __init__(self, pricing_rules):
        self.items = []
        self.pricing_rules = pricing_rules

    @staticmethod
    def load_rules(self, file_path):
        with open(file_path, 'r') as file:
            dt = json.load(file)

        pricing_rules = {}
        # creating discounts here
        return pricing_rules

    def scan(self, item):
        self.items.append(item)

    def total(self):
        pass
