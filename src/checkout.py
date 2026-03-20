# src/checkout.py

class CheckoutService:
    def __init__(self, cart, payment_gateway):
        self.cart = cart
        self.payment_gateway = payment_gateway

    def process(self, token):
        # Validate inventory
        if self.cart.inventory:
            for sku, qty in self.cart.items.items():
                available = self.cart.inventory.getAvailable(sku)
                if qty > available:
                    return {"status": "failure", "error": "Insufficient inventory"}

        # Compute total after discounts
        total = self.cart.total_with_discounts()

        # Attempt payment
        success = self.payment_gateway.charge(total, token)
        if success:
            return {"status": "success", "charged_amount": total}
        else:
            return {"status": "failure", "error": "Payment failed"}

# src/fake_gateways.py

class FakePaymentGateway:
    def __init__(self, success=True):
        self.success = success

    def charge(self, amount, token):
        return self.success