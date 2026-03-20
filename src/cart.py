# src/cart.py
class Cart:
    def __init__(self, catalog):
        self.catalog = catalog
        self.items = {}

    def add(self, sku, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        product = self.catalog.get(sku)
        if not product:
            raise ValueError("Product not found")

        self.items[sku] = self.items.get(sku, 0) + quantity

    def remove(self, sku):
        if sku in self.items:
            del self.items[sku]

    def total(self):
        total = 0
        for sku, qty in self.items.items():
            product = self.catalog.get(sku)
            total += product.price * qty
        return total