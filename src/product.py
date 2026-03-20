# src/product.py
class Product:
    def __init__(self, sku, name, price):
        if price < 0:
            raise ValueError("Invalid price")
        self.sku = sku
        self.name = name
        self.price = price