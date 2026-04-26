from src.problems.graphs.num_island import num_islands

def test_num_island():
    grid = [
        ["1", "0"],
        ["0", "1"]
    ]
    assert num_islands(grid) == 2
