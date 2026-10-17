from addition import addition

def test_addition_positive():
    assert addition(3, 5) == 8

def test_addition_negative():
    assert addition(-1, 1) == 0
