from graph.travarse import Graph

def test_print_graph():
    g = Graph()
    g.addVertex(0)
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    g.addVertex(6)
    g.addEdge(0,1)
    g.addEdge(0,4)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(5,6)
    # g.printGraph()

    res = g.dfs(0)
    print(res)

