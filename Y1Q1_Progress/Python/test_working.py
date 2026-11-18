from working import convert
import pytest

def test_convert_allvalid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_convert_invalidtime():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_convert_invalidstr():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_convert_invalidall():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
