# tests/test_inventory.py
import pytest
from unittest.mock import Mock
from src.cart import Cart
from src.product import Product

def test_insufficient_inventory():
    # mock catalog
    catalog = Mock()
    catalog.get.return_value = Product("SKU1", "Item1", 100)

    # mock inventory
    inventory = Mock()
    inventory.getAvailable.return_value = 1

    cart = Cart(catalog, inventory)

    # trying to add more than available stock
    with pytest.raises(ValueError):
        cart.add("SKU1", 2)