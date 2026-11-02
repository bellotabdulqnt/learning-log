from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 0.75

def test_convert_exceptions():
    with pytest.raises((ZeroDivisionError, ValueError)):
        convert("3/0")
        convert("cat/dog")

def test_gauge():
    assert gauge(0.75) == "75%"

def test_gauge_full():
    assert gauge(0.99) == "F"

def test_gauge_empty():
    assert gauge(0.01) == "E"

def test_gauge_error():
    with pytest.raises(ValueError):
        gauge(-3/4)
        gauge(4/3)
