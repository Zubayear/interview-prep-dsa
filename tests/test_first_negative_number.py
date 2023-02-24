from sliding_window.first_negative_number import first_neg_number

def test_first_neg_number():
    assert first_neg_number([-8,2,3,-6,10], 2) == [-8,0,-6,-6]
    assert first_neg_number([12, -1, -7, 8, -15, 30, 16, 28], 3) == [-1, -1, -7, -15, -15, 0 ]