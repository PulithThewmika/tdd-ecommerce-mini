# tests/test_cart.py
import pytest
from src.cart import Cart
from src.product import Product

class FakeCatalog:
    def __init__(self):
        self.products = {"SKU1": Product("SKU1", "Item1", 100)}

    def get(self, sku):
        return self.products.get(sku)


def test_add_item():
    cart = Cart(FakeCatalog())
    cart.add("SKU1", 2)
    assert cart.total() == 200


def test_remove_item():
    cart = Cart(FakeCatalog())
    cart.add("SKU1", 2)
    cart.remove("SKU1")
    assert cart.total() == 0


def test_invalid_quantity():
    cart = Cart(FakeCatalog())
    with pytest.raises(ValueError):
        cart.add("SKU1", 0)


def test_product_not_found():
    cart = Cart(FakeCatalog())
    with pytest.raises(ValueError):
        cart.add("UNKNOWN", 1)