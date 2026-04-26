import collections


def oranges_rotting(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = collections.deque()
    time, fresh_oranges = 0, 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh_oranges += 1
            if grid[r][c] == 2:
                queue.append((r, c))

    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while fresh_oranges > 0 and queue:
        length = len(queue)
        time += 1
        for _ in range(length):
            r, c = queue.popleft()
            for x, y in dirs:
                row, col = r + x, c + y
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                    continue
                grid[row][col] = 2
                queue.append((row, col))
                fresh_oranges -= 1

    return -1 if fresh_oranges > 0 else time
