import threading

class InventoryManager:
    def __init__(self, initial_stock=None):
        self.stock = initial_stock or {}
        self.lock = threading.Lock()
        
    def add_product(self, sku, quantity):
        with self.lock:
            self.stock[sku] = self.stock.get(sku, 0) + quantity
            
    def getAvailable(self, sku):
        with self.lock:
            return self.stock.get(sku, 0)
            
    def reserve(self, sku, quantity):
        """Returns True if successfully reserved, False otherwise."""
        with self.lock:
            if self.stock.get(sku, 0) >= quantity:
                self.stock[sku] -= quantity
                return True
            return False
