import pytest
from src.phone import Phone

@pytest.fixture
def phone_obj():
    return Phone("iPhone 18", 150_000, 7, 4)

def test__repr__(phone_obj):
    assert phone_obj.__repr__() == "Phone('iPhone 18', 150000, 7, 4)"

def test__str__(phone_obj):
    assert phone_obj.__str__() == 'iPhone 18'

def test__init__(phone_obj):
    assert phone_obj.number_of_sim == 4