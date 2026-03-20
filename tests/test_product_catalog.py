# tests/test_product_catalog.py
import pytest
from src.product import Product
from src.catalog import Catalog

def test_create_product_invalid_price():
    with pytest.raises(ValueError):
        Product("SKU1", "Item1", -10)