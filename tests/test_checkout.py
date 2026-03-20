# tests/test_checkout.py
from src.cart import Cart
from src.checkout import CheckoutService

class FakeProduct:
    def __init__(self, sku, price):
        self.sku = sku
        self.price = price

class FakeCatalog:
    def __init__(self):
        self.products = {"SKU1": FakeProduct("SKU1", 100)}
    def get(self, sku):
        return self.products.get(sku)

class FakeInventory:
    def getAvailable(self, sku):
        return 100

class FakePaymentGateway:
    def __init__(self, success=True):
        self.success = success
    def charge(self, amount, token):
        return self.success

def test_successful_checkout():
    catalog = FakeCatalog()
    cart = Cart(catalog, FakeInventory())
    cart.add("SKU1", 2)
    gateway = FakePaymentGateway(success=True)
    
    checkout = CheckoutService(cart, gateway)
    result = checkout.process("token123")
    
    assert result["status"] == "success"
    assert result["charged_amount"] == cart.total_with_discounts()

def test_payment_failure_checkout():
    catalog = FakeCatalog()
    cart = Cart(catalog, FakeInventory())
    cart.add("SKU1", 2)
    gateway = FakePaymentGateway(success=False)
    
    checkout = CheckoutService(cart, gateway)
    result = checkout.process("token123")
    
    assert result["status"] == "failure"
    assert "error" in result