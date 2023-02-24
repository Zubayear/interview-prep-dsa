from graph.custom_graph import Graph


def test_create_graph():
    # g = Graph(9)
    #
    # g.add_edge(1, 2)
    # g.add_edge(1, 6)
    # g.add_edge(2, 3)
    # g.add_edge(2, 4)
    # g.add_edge(4, 5)
    # g.add_edge(5, 8)
    # g.add_edge(6, 7)
    # g.add_edge(6, 9)
    # g.add_edge(7, 8)
    #
    # res = g.bfs_traversal(1)
    # print(res)
    digraph = {
        0: [2, 3],
        1: [4],
        2: [1, 3],
        3: [1],
        4: [],
        5: [1, 4]
    }
    actual = Graph.topological_sort(digraph)
    assert actual == [0, 5, 2, 3, 1, 4]
