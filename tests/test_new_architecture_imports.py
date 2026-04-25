from patterns.dp import Solution
from patterns.graph.traversal import Graph as TraversalGraph
from patterns.sliding_window.find_maximum_in_sliding_window import (
    find_max_sliding_window,
)
from structures.stack import Stack
from structures.tree import BST


def test_canonical_packages_import():
    assert Solution.rob([2, 7, 9, 3, 1]) == 12
    assert find_max_sliding_window([-4, 2, -5, 3, 6], 3) == [2, 3, 6]


def test_canonical_structures_import():
    stack = Stack()
    assert stack.push(1) is True
    bst = BST()
    bst.insert_iter(2)
    bst.insert_iter(1)
    bst.insert_iter(3)
    assert bst.bfs(bst.root) == [[2], [1, 3]]


def test_canonical_graph_import():
    graph = TraversalGraph()
    for vertex in range(3):
        graph.add_vertex(vertex)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    assert graph.bfs(0) == [0, 1, 2]
