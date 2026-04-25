from patterns.arrays_hashing.max_cpu_load import max_cpu_load


def test_max_cpu_load():
    # jobs1 = [[1, 4, 3], [2, 6, 4], [5, 9, 6]]
    jobs1 = [[2, 4, 5], [0, 6, 7], [5, 10, 6]]
    jobs2 = [[2, 4, 5], [0, 6, 7], [5, 10, 6], [0, 3, 10]]
    assert max_cpu_load(jobs1) == 13
    assert max_cpu_load(jobs2) == 22
