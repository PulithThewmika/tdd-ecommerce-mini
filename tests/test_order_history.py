# tests/test_order_history.py

import datetime

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