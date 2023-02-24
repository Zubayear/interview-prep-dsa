class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.graph.keys() and vertex2 in self.graph.keys():
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def printGraph(self):
        for v in self.graph:
            print(v, ":", self.graph[v])

    def bfs(self, start):
        result = []
        if start is None or start not in self.graph.keys():
            return result
        q = []
        visited = set()
        q.append(start)
        visited.add(start)

        while len(q):
            currentVal = q.pop(0)
            result.append(currentVal)
            for i in self.graph[currentVal]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)
        return result

    def dfs(self, start):
        result = []
        if start is None or start not in self.graph.keys():
            return result
        stack = []
        visited = set()
        stack.append(start)
        visited.add(start)

        while len(stack):
            currentValue = stack.pop()
            result.append(currentValue)
            for i in self.graph[currentValue]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
        return result
