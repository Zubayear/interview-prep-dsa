from algo_expert.maxCPULoad import maxCPULoad


def test_MaxCPULoad():
    # jobs1 = [[1, 4, 3], [2, 6, 4], [5, 9, 6]]
    jobs1 = [[2, 4, 5], [0, 6, 7], [5, 10, 6]]
    jobs2 = [[2, 4, 5], [0, 6, 7], [5, 10, 6], [0, 3, 10]]
    assert maxCPULoad(jobs1) == 13
    assert maxCPULoad(jobs2) == 22
