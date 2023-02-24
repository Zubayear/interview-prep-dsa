import collections


def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = collections.deque()
    time, fresh_oranges = 0, 0

    # add rotten oranges in the queue
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh_oranges += 1
            if grid[r][c] == 2:
                queue.append((r, c))

    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # loop through queue and make the fresh oranges rotten
    while fresh_oranges > 0 and queue:
        length = len(queue)
        time += 1
        for i in range(length):
            r, c = queue.popleft()

            # make the oranges in all 4 directions rotten
            for x, y in dirs:
                row, col = r + x, c + y
                # checking if its out of boundary or if its not fresh
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                    continue
                grid[row][col] = 2
                queue.append((row, col))
                fresh_oranges -= 1

    return time
