from graph.number_of_provinces import find_circle_num


def test_find_circle_num():
    is_connected = [[1,1,0],[1,1,0],[0,0,1]]
    # x = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    assert find_circle_num(is_connected) == 2
    # assert find_circle_num(x) == 5