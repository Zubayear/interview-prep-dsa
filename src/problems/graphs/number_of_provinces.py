from typing import List


def find_circle_num(is_connected: List[List[int]]) -> int:
    n = len(is_connected)
    parent = [i for i in range(n)]
    rank = [1] * n
    res = n

    def find(x: int) -> int:
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> int:
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return 0
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_y] > rank[root_x]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return 1

    for i in range(n):
        for j in range(len(is_connected[0])):
            if is_connected[i][j] == 1:
                res -= union(i, j)
    return res
