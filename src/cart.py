# src/cart.py
class Cart:
    def __init__(self, catalog, inventory=None):
        self.catalog = catalog
        self.inventory = inventory
        self.items = {}  # {sku: quantity}

    def add(self, sku, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        product = self.catalog.get(sku)
        if not product:
            raise ValueError("Product not found")

        # inventory check
        if self.inventory:
            available = self.inventory.getAvailable(sku)
            if quantity > available:
                raise ValueError("Insufficient inventory")

        self.items[sku] = self.items.get(sku, 0) + quantity

    def remove(self, sku):
        """Remove item completely from cart"""
        if sku in self.items:
            del self.items[sku]

    def total(self):
        """Compute total of cart items"""
        total_price = 0
        for sku, qty in self.items.items():
            product = self.catalog.get(sku)
            total_price += product.price * qty
        return total_price

    def total_with_discounts(self):
        """Compute total with discount rules applied"""
        from src.discount import DiscountEngine, BulkDiscountRule, OrderDiscountRule
        engine = DiscountEngine()
        engine.add_rule(BulkDiscountRule())
        engine.add_rule(OrderDiscountRule())
        return engine.apply(self)