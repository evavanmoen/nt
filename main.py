from checkout.checkout import Checkout


def main():
    pricing_rules = Checkout.load_rules('pricing_rules/ex1.json')

    checkout = Checkout(pricing_rules)
    checkout.scan('VOUCHER')
    checkout.scan('TSHIRT')
    checkout.scan('PANTS')
    print(f"Total: {checkout.total()}€")  # Expected: 'Total: 32.50€'


if __name__ == "__main__":
    main()

