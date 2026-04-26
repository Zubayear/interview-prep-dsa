from collections import deque
from typing import List


class Graph:
    def __init__(self, vertices=None) -> None:
        if vertices is None:
            self.graph = {}
        else:
            self.graph = {node + 1: [] for node in range(vertices)}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def add_edges(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        for v in self.graph:
            print(v, ":", self.graph[v])

    def bfs(self, start):
        result = []
        if start is None or start not in self.graph:
            return result
        q = [start]
        visited = {start}
        while q:
            current_val = q.pop(0)
            result.append(current_val)
            for i in self.graph[current_val]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)
        return result

    def dfs(self, start):
        result = []
        if start is None or start not in self.graph:
            return result
        stack = [start]
        visited = {start}
        while stack:
            current_val = stack.pop()
            result.append(current_val)
            for i in self.graph[current_val]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
        return result

    def bfs_traversal(self, start: int) -> List[int]:
        return self.bfs(start)

    def dfs_traversal(self, start: int) -> List[int]:
        return self.dfs(start)

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
