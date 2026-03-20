# tests/test_order_history.py

import datetime
from src.cart import Cart
from src.checkout import CheckoutService
from src.order import FakeOrderRepository

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

def test_checkout_creates_order():
    catalog = FakeCatalog()
    inventory = FakeInventory()
    cart = Cart(catalog, inventory)
    cart.add("SKU1", 2)
    gateway = FakePaymentGateway(success=True)
    fake_repo = FakeOrderRepository()

    checkout = CheckoutService(cart, gateway, order_repo=fake_repo)
    result = checkout.process("token123")

    assert result["status"] == "success"
    assert len(fake_repo.saved_orders) == 1
    order = fake_repo.saved_orders[0]
    assert order.total == cart.total_with_discounts()
    assert "SKU1" in order.items
    assert isinstance(order.timestamp, datetime.datetime)