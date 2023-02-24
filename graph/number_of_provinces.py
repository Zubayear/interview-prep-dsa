from typing import List


def find_circle_num(is_connected: List[List[int]]) -> int:
    """
    implementation of quick union
    """
    n = len(is_connected)
    parent = [i for i in range(n)] # keep the parent
    rank = [1] * n
    res = n

    def find(x: int) -> int:
        """
        0
        |
        1
        |
        2
        |
        3
        |
        4
        |
        5

        for finding the root of 5 we'll find the root of 4, 3, 2, 1
        so at first call we'll make something like this
            0
        / | | | \
        1 2 3 4  5
        """
        if x == parent[x]: # check if parent node of x is equal to itself
            return x
        # path compression
        # first call we'll find the root of 5
        parent[x] = find(parent[x]) # call with 4 then 4, then 3 ... this will return the parent and we assign them
        return parent[x] # return the parent of 5
    
    def union(x: int, y: int) -> int:
        # find the root of x and y
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return 0
        # find the rank and make higher rank the parent & increase its rank by 1
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_y] > rank[root_x]:
            parent[root_x] = root_y
        else:
            # make either one
            parent[root_y] = root_x
            rank[root_x] += 1
        return 1
    
    for i in range(n):
        for j in range(len(is_connected[0])):
            if is_connected[i][j] == 1:
                res -= union(i, j)
    return res
