import threading
import pytest
from src.inventory import InventoryManager

def test_concurrent_reservations():
    inventory = InventoryManager({"SKU1": 100})
    
    # We will simulate 100 threads trying to reserve 1 item each
    # and 50 threads trying to reserve an extra 1 (these will fail for some if they exceed 100 total)
    
    success_count = 0
    fail_count = 0
    lock = threading.Lock()
    
    def worker():
        nonlocal success_count, fail_count
        if inventory.reserve("SKU1", 1):
            with lock:
                success_count += 1
        else:
            with lock:
                fail_count += 1
                
    threads = []
    # 150 workers trying to take 1 item from stock of 100
    for _ in range(150):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    assert success_count == 100, f"Expected 100 successful reservations, got {success_count}"
    assert fail_count == 50, f"Expected 50 failed reservations, got {fail_count}"
    assert inventory.getAvailable("SKU1") == 0
