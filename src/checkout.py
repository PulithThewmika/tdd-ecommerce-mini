# src/checkout.py
from src.order import Order

class CheckoutService:
    def __init__(self, cart, payment_gateway, order_repo=None):
        self.cart = cart
        self.payment_gateway = payment_gateway
        self.order_repo = order_repo

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
            if self.order_repo:
                order = Order(self.cart.items, total)
                self.order_repo.save(order)
            return {"status": "success", "charged_amount": total}
        else:
            return {"status": "failure", "error": "Payment failed"}

# src/fake_gateways.py

class FakePaymentGateway:
    def __init__(self, success=True):
        self.success = success

    def charge(self, amount, token):
        return self.success