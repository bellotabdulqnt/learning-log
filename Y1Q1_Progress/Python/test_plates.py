from plates import is_valid
def test_isvalid():
    assert is_valid("CS50")

def test_isvalid_punct():
    assert not is_valid("PI3.14")

def test_isvalid_long():
    assert not is_valid("OUTATIME")