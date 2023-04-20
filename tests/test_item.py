import pytest
from src.item import Item
from src.phone import Phone

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
    assert item_obj.__repr__() == "Item('Пылесос', 1000, 20)"

def test___str__(item_obj):
    assert Item.__str__(item_obj) == 'Пылесос'


@pytest.fixture
def phone_obj():
    return Phone("iPhone 18", 150_000, 7, 4)

def test__repr__(phone_obj):
    assert phone_obj.__repr__() == "Phone('iPhone 18', 150000, 7, 4)"

def test__str__(phone_obj):
    assert phone_obj.__str__() == 'iPhone 18'

def test__init__(phone_obj):
    assert phone_obj.number_of_sim == 4