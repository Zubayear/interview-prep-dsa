from collections import deque
from typing import List


class Graph:
    """graph class
    """

    def __init__(self, vertices) -> None:
        self.graph = {node+1: [] for node in range(vertices)}

    def add_edge(self, vertex1: int, vertex2: int) -> bool:
        """add two vertices

        Args:
            vertex1 (int): first vertex
            vertex2 (int): second vertex

        Returns:
            bool: return True if added successfully
        """
        if vertex1 in self.graph.keys() and vertex2 in self.graph.keys():
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            return True
        return False

    def print_graph(self) -> None:
        """print the graph
        """
        for node in self.graph:
            print(node, ":", self.graph[node])

    def bfs_traversal(self, start: int) -> List[int]:
        """return the bfs traversal of a graphs

        Args:
            start (int): start node

        Returns:
            List[int]: result of bfs traversal
        """
        bfs_traversal_result = []
        visited = set()
        queue = deque([])
        visited.add(start)
        queue.append(start)

        while queue:
            node = queue.popleft()
            bfs_traversal_result.append(node)
            # visit all neighbor
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return bfs_traversal_result

    def dfs_traversal(self, start: int) -> List[int]:
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
        """
        0 -> [2,3]\n
        1 -> [4]\n
        2 -> [1,3]\n
        3 -> [1]\n
        4 -> []\n
        5 -> [1,4]
        @param digraph:
        @return:
        """
        # node -> no of indegrees
        indegrees = {node: 0 for node in digraph}

        # increment the value (of node in the right of digraph) in indegrees map
        for node in digraph:
            for neighbor in digraph[node]:
                indegrees[neighbor] += 1

        topological_ordering = []
        nodes_with_no_incoming_edges = deque([])

        # calculate node with no incoming edges i.e. indegree zero
        for node in digraph:
            if indegrees[node] == 0:
                nodes_with_no_incoming_edges.append(node)

        while nodes_with_no_incoming_edges:
            """
            start at zero indegree node
            go to it's neighbors and decrement their indegree by 1
            if any neighbor's indegree becomes zero then add it to the queue for process
            """
            node = nodes_with_no_incoming_edges.popleft()
            topological_ordering.append(node)

            for neighbor in digraph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    nodes_with_no_incoming_edges.append(neighbor)

        if len(topological_ordering) == len(digraph):
            return topological_ordering
        else:
            raise Exception("There might be a cycle in the graph")
