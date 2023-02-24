from graph.oranges_rotting import orangesRotting


def test_orangesRotting():
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    assert orangesRotting(grid) == 4
