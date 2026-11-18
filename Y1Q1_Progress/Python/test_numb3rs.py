from numb3rs import validate
import pytest

def test_validate_right():
    assert validate("25.255.255.0")

def test_validate_wrongdigit():
    assert not validate("512.512.512.512")
    assert not validate("192.168.001.1")

def test_validate_invalid():
    with pytest.raises((AttributeError, ValueError)):
        validate("255.255.255.255.255")
        validate("....")