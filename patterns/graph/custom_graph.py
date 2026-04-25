from collections import deque
from typing import List


class Graph:
    def __init__(self, vertices=None) -> None:
        if vertices is None:
            self.graph = {}
        else:
            self.graph = {node + 1: [] for node in range(vertices)}

    def add_edges(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def add_edge(self, vertex1: int, vertex2: int) -> bool:
        if vertex1 in self.graph.keys() and vertex2 in self.graph.keys():
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            return True
        return False

    def print_graph(self) -> None:
        for node in self.graph:
            print(node, ":", self.graph[node])

    def bfs_traversal(self, start: int) -> List[int]:
        if start not in self.graph:
            return []
        bfs_traversal_result = []
        visited = set()
        queue = deque([])
        visited.add(start)
        queue.append(start)

        while queue:
            node = queue.popleft()
            bfs_traversal_result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return bfs_traversal_result

    def dfs_traversal(self, start: int) -> List[int]:
        if start not in self.graph:
            return []
        dfs_traversal_result = []
        visited = set()
        stack = deque([])
        stack.append(start)
        visited.add(start)

        while stack:
            node = stack.pop()
            dfs_traversal_result.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
        return dfs_traversal_result

    @staticmethod
    def topological_sort(digraph) -> List[int]:
        indegrees = {node: 0 for node in digraph}
        for node in digraph:
            for neighbor in digraph[node]:
                indegrees[neighbor] += 1

        topological_ordering = []
        nodes_with_no_incoming_edges = deque([])
        for node in digraph:
            if indegrees[node] == 0:
                nodes_with_no_incoming_edges.append(node)

        while nodes_with_no_incoming_edges:
            node = nodes_with_no_incoming_edges.popleft()
            topological_ordering.append(node)
            for neighbor in digraph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    nodes_with_no_incoming_edges.append(neighbor)

        if len(topological_ordering) == len(digraph):
            return topological_ordering
        raise Exception("There might be a cycle in the graph")
