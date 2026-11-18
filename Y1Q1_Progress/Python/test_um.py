from um import count

def test_count_noum():
    assert count("referendum") == 0

def test_count_hasum():
    assert count("um") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1