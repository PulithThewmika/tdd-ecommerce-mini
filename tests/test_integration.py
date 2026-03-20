import pytest
from src.cart import Cart
from src.checkout import CheckoutService
from src.inventory import InventoryManager
from src.order_repository import SQLiteOrderRepository

class RealProduct:
    def __init__(self, sku, price):
        self.sku = sku
        self.price = price

class RealCatalog:
    def __init__(self):
        self.products = {
            "INTEG_SKU1": RealProduct("INTEG_SKU1", 100),
            "INTEG_SKU2": RealProduct("INTEG_SKU2", 50)
        }
    def get(self, sku):
        return self.products.get(sku)

class DummyPaymentGateway:
    def charge(self, amount, token):
        # Always succeed for integration
        return True

def test_full_checkout_flow_with_db():
    # 1. Setup Data store
    repo = SQLiteOrderRepository(":memory:")
    
    # 2. Setup Catalog and Inventory
    catalog = RealCatalog()
    inventory = InventoryManager({"INTEG_SKU1": 10, "INTEG_SKU2": 5})
    
    # 3. Setup Cart
    cart = Cart(catalog, inventory)
    
    # 4. Add items
    cart.add("INTEG_SKU1", 2) # 2 * 100 = 200
    cart.add("INTEG_SKU2", 3) # 3 * 50 = 150
    # Gross total = 350
    
    # 5. Checkout
    gateway = DummyPaymentGateway()
    checkout_service = CheckoutService(cart, gateway, order_repo=repo)
    
    result = checkout_service.process("tok_123")
    
    assert result["status"] == "success"
    assert result["charged_amount"] == 350
    
    # 6. Verify Database
    saved_orders = repo.get_all()
    assert len(saved_orders) == 1
    assert saved_orders[0].total == 350
    assert saved_orders[0].items == {"INTEG_SKU1": 2, "INTEG_SKU2": 3}

    # 7. Verify Inventory was reduced by checkout
    assert inventory.getAvailable("INTEG_SKU1") == 8
    assert inventory.getAvailable("INTEG_SKU2") == 2
