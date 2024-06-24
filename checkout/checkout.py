import json


class Checkout:
    def __init__(self, pricing_rules):
        """
        Initializes a Checkout instance.

        Args:
            pricing_rules (dict): A dictionary containing pricing rules for items
        """
        self.items = []  # initialize an empty list
        self.pricing_rules = pricing_rules  # reload pricing rules for item pricing

    def scan(self, item):
        """
        Adds an item to the list of scanned items.

        Args:
            item (str): The item to be added
        """
        self.items.append(item)

    def total(self):
        """
        Calculates the total cost of scanned items based on pricing rules.

        Returns:
            float: The total cost of all scanned items after applying any discounts
        """
        total = 0
        # count occurrences of each item in the list of scanned items
        item_counts = {item: self.items.count(item) for item in set(self.items)}

        for item, count in item_counts.items():
            # get pricing rule for the current item
            rule = self.pricing_rules.get(item, None)
            if rule:
                if 'apply_discount' in rule:
                    # apply discount if specified in pricing rule
                    discount_params = {var: rule[var] for var in rule
                                       if var in ['price', 'min_items', 'discount_amount']}
                    total += rule['apply_discount'](count=count, **discount_params)
                else:
                    # calculate case total if no discount
                    total += count * rule['price']

        return total

    @staticmethod
    def load_rules(file_path):
        """
        Loads pricing rules from a JSON file.

        Args:
            file_path (str): The path to the JSON file containing pricing rules

        Returns:
            dict: A dictionary containing pricing rules loaded from the JSON file
        """
        # load pricing rules from a JSON file
        with open(file_path, 'r') as file:
            dt = json.load(file)

        # parse rules from data read and create our pricing_rules
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
        """
        Applies "2 for 1" discount calculation.

        Args:
            price (float): The price per item
            count (int): The number of items

        Returns:
            float: The total cost after applying the "2 for 1" discount
        """
        return (count // 2 + count % 2) * price

    @staticmethod
    def _apply_discount_bulk(min_items, discount_amount, price, count):
        """
        Applies bulk discount calculation.

        Args:
            min_items (int): The minimum number of items required for the discount
            discount_amount (float): The amount to discount per item
            price (float): The price per item
            count (int): The number of items

        Returns:
            float: The total cost after applying the bulk discount
        """
        if count >= min_items:
            return count * (price - discount_amount)
        else:
            return count * price

