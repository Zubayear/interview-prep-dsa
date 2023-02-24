from graph.numIsland import numIslands

def test_numIsland():
    grid = [
        ["1", "0"],
        ["0", "1"]
    ]
    assert numIslands(grid) == 2