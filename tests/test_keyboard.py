import pytest

from src.keyboard import Keyboard, LanguageMixin

@pytest.fixture
def keyboard_obj():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test__repr__(keyboard_obj):
    assert keyboard_obj.__repr__() == "Keyboard('Dark Project KD87A', 9600, 5)"

def test__str__(keyboard_obj):
    assert keyboard_obj.__str__() == 'Dark Project KD87A'
    assert str(keyboard_obj.language) == "EN"

def test_change_lang(keyboard_obj):
    keyboard_obj.change_lang()
    assert str(keyboard_obj.language) == "RU"
    keyboard_obj.change_lang().change_lang()
    assert str(keyboard_obj.language) == "RU"





