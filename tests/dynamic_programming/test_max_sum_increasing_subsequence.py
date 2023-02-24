from dynamic_programming.max_sum_increasing_subsequence import max_sum_increasing_subsequence

def test_max_sum_increasing_subsequence():
    assert max_sum_increasing_subsequence([8,12,2,3,15,5,7]) == (35, [8,12,15])
