from patterns.graph.oranges_rotting import oranges_rotting


def test_oranges_rotting():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    assert oranges_rotting(grid) == 4


def test_oranges_rotting_unreachable():
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    assert oranges_rotting(grid) == -1
