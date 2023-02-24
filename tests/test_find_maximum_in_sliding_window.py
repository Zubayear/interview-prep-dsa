from sliding_window.find_maximum_in_sliding_window import \
    find_max_sliding_window


def test_find_max_sliding_window():
    assert find_max_sliding_window([-4,2,-5,3,6],3) == [2,3,6]
    # assert find_max_sliding_window([-4, 5, 4, -4, 4, 6, 7],2) == [5, 5, 4, 4, 6, 7]
    # assert find_max_sliding_window([-4, 5, 4, -4, 4 , 6, 7],10) == [7]
    # assert find_max_sliding_window([-4,2,-5,3,6],3) == [2,3,6]