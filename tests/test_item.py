import pytest
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


def testInit():
    itm=Item("Утюг", 1000, 20)
    assert itm.name == "Утюг"
    assert itm.price == 1000
    assert itm.quantity == 20
@pytest.fixture
def itm():
    return "Утюг", 1000, 20
def test_calculate_total_price_(itm):
    assert itm.calculate_total_price(itm) == 20000

def test_apply_discount(itm):
    pay_rate = 0.5
    assert itm.apply_discount(itm) == 500

