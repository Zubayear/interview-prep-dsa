from algo_expert.sorted_squared_array import squared_array

def test_squared_array():
    assert squared_array([-1,-1,2,3]) == [1,1,4,9]
    assert squared_array([-6,-1,2,3]) == [1,4,9,36]
    assert squared_array([-9, -8, 0]) == [0, 64, 81]