import pytest
from bank import value

def test_value_hello():
    assert value("Hello") == "$0"

def test_value_h():
    assert value("Hi") == "$20"

def test_value_neither():
    assert value("What's up?") == "$100"