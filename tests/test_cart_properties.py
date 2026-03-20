import pytest
from hypothesis import given, strategies as st
from src.cart import Cart

class FakeProduct:
    def __init__(self, sku, price):
        self.sku = sku
        self.price = price

class FakeCatalog:
    def __init__(self):
        self.products = {
            "SKU_A": FakeProduct("SKU_A", 10),
            "SKU_B": FakeProduct("SKU_B", 25),
            "SKU_C": FakeProduct("SKU_C", 100),
        }
    def get(self, sku):
        return self.products.get(sku)

@given(st.lists(
    st.tuples(
        st.sampled_from(["SKU_A", "SKU_B", "SKU_C"]),
        st.integers(min_value=1, max_value=100)
    )
))
def test_cart_total_always_non_negative_and_additive(item_batches):
    catalog = FakeCatalog()
    cart = Cart(catalog)
    
    expected_total = 0
    for sku, qty in item_batches:
        cart.add(sku, qty)
        expected_total += catalog.get(sku).price * qty
        
    assert cart.total() == expected_total
    assert cart.total() >= 0
