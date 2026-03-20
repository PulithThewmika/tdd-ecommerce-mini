# tests/test_discount.py
from src.cart import Cart  

# FakeCatalog for testing
class FakeProduct:
    def __init__(self, sku, price):
        self.sku = sku
        self.price = price

class FakeCatalog:
    def __init__(self):
        self.products = {"SKU1": FakeProduct("SKU1", 100)}

    def get(self, sku):
        return self.products.get(sku)

# Now tests can use Cart and FakeCatalog
def test_bulk_discount():
    catalog = FakeCatalog()
    cart = Cart(catalog)
    cart.add("SKU1", 10)  
    catalog.products["SKU2"] = FakeProduct("SKU2", 50)
    cart2 = Cart(catalog)
    cart2.add("SKU2", 10) 
    assert cart2.total_with_discounts() == 450  

def test_order_discount():
    catalog = FakeCatalog()
    cart = Cart(catalog)
    catalog.products["SKU2"] = FakeProduct("SKU2", 550)
    cart.add("SKU1", 1)  
    cart.add("SKU2", 2)  
    assert cart.total_with_discounts() == 1140 