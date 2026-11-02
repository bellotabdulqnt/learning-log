import pytest
from twttr import shorten

def test_shorten_lower():
    assert shorten("Twitter") == "Twttr"

def test_shorten_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_shorten_novowels():
    assert shorten("Rhythm") == "Rhythm"