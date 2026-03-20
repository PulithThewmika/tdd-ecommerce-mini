# src/order.py
import datetime

class Order:
    def __init__(self, items, total):
        self.items = items.copy()
        self.total = total
        self.timestamp = datetime.datetime.now()

# src/order_repository.py
class FakeOrderRepository:
    def __init__(self):
        self.saved_orders = []

    def save(self, order):
        self.saved_orders.append(order)

# src/checkout.py
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
        if not success:
            return {"status": "failure", "error": "Payment failed"}

        # Create order
        if self.order_repo:
            order = Order(self.cart.items, total)
            self.order_repo.save(order)

        return {"status": "success", "charged_amount": total}