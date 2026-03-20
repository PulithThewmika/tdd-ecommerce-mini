# tests/test_checkout.py

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