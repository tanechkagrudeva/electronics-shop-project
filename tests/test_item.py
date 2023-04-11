import pytest
from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""

@pytest.fixture
def item_obj():
    return Item('Пылесос', 1000, 20)
def test_init(item_obj):
    assert item_obj.price == 1000
    assert item_obj.quantity == 20

def test_calculate_total_price(item_obj):
    assert item_obj.calculate_total_price() == 20000

def test_apply_discount(item_obj):
    assert item_obj.apply_discount() == 1000

def test_string_to_number(item_obj):
    assert Item.string_to_number(7.1) == 7

def test___repr__(item_obj):
    assert Item.__repr__(item_obj) == "Item('Пылесос', 1000, 20)"

def test___str__(item_obj):
    assert Item.__str__(item_obj) == 'Пылесос'


