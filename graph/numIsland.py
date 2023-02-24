import collections
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    row, col = len(grid), len(grid[0])
    island = 0
    visited = set()

    def dfs(r, c):
        if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == '0':
            print(r, c, grid)
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    def bfs(r, c):
        q = collections.deque()
        visited.add((r, c))
        q.append((r, c))
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while len(q):
            x, y = q.popleft()
            for d1, d2 in dirs:
                v1, v2 = x + d1, y + d2
                if (v1 in range(row) and
                        v2 in range(col) and
                        grid[v1][v2] == "1" and
                        (v1, v2) not in visited):
                    visited.add((v1, v2))
                    q.append((v1, v2))

    for i in range(0, row):
        for j in range(0, col):
            if grid[i][j] == '1' and (i, j) not in visited:
                bfs(i, j)
                island += 1
    return island
