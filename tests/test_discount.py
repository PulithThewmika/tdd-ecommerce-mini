# test_discount.py
def test_bulk_discount():
    catalog = FakeCatalog()
    cart = Cart(catalog)
    cart.add("SKU1", 10)  # 10 items
    discount_engine = DiscountEngine()
    discount_engine.add_rule(BulkDiscountRule())
    total = discount_engine.apply(cart)
    assert total == 10 * 100 * 0.9  # 10% off on line

def test_order_discount():
    catalog = FakeCatalog()
    cart = Cart(catalog)
    cart.add("SKU1", 10)  # 10 * 100 = 1000
    discount_engine = DiscountEngine()
    discount_engine.add_rule(OrderDiscountRule())
    total = discount_engine.apply(cart)
    assert total == 1000 * 0.95  # 5% off on order