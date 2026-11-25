from seasons import minutegrab
import pytest

def test_minutegrab_valid():
    assert minutegrab("2025-11-25") == 525600
    assert minutegrab("2024-11-25") == 1051200

def test_minutegrab_invalid():
    with pytest.raises((AttributeError, ValueError)):
        minutegrab("")
        minutegrab("January 1, 1999")
        minutegrab("2020-15-33")
