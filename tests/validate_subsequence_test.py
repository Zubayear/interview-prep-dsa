from algo_expert.validate_subsequence import is_valid_sequence

def test_is_valid_sequence():
    assert is_valid_sequence([5, 1, 22, 25, 6, -1, -18, 10], [1, 6, -1, 10]) == True
    assert is_valid_sequence([5, 1, 22, 25, 10, 6, -18], [1, 6, 10]) == False
    assert is_valid_sequence([], []) == True
    assert is_valid_sequence([], [1]) == False
    assert is_valid_sequence([0], [1]) == False
    assert is_valid_sequence([5, 1, 22, 25, 6, -1, -18, 10], [23]) == False
    assert is_valid_sequence([23], [23, 90]) == False