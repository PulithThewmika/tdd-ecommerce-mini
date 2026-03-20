# src/catalog.py
class Catalog:
    def __init__(self):
        self.products = {}

    def add(self, product):
        self.products[product.sku] = product

    def get(self, sku):
        return self.products.get(sku)