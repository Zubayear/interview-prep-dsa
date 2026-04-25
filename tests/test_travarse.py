from patterns.graph.traversal import Graph


def test_print_graph():
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_edge(0,1)
    g.add_edge(0,4)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(3,5)
    g.add_edge(5,6)
    assert g.bfs(0) == [0, 1, 4, 2, 3, 5, 6]
    assert g.dfs(0) == [0, 4, 3, 5, 6, 2, 1]
