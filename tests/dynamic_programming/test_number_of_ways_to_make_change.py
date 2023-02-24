from dynamic_programming.number_of_ways_to_make_change import number_of_ways_to_make_change

def test_number_of_ways_to_make_change():
    actual = number_of_ways_to_make_change(10, [1, 5, 10, 25])
    assert actual == 4
