# src/discount.py

class DiscountEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def apply(self, cart):
        total = cart.total()
        for rule in self.rules:
            total = rule.apply(cart, total)
        return total

class BulkDiscountRule:
    def apply(self, cart, current_total):
        total = 0
        for sku, qty in cart.items.items():
            product = cart.catalog.get(sku)
            line_total = product.price * qty
            if qty >= 10:
                line_total *= 0.9  # 10% off
            total += line_total
        return total

class OrderDiscountRule:
    def apply(self, cart, current_total):
        if cart.total() >= 1000:
            return current_total * 0.95  # 5% off order
        return current_total
        return current_total