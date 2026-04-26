import pytest

from src.data_structures.trees import BST


@pytest.fixture()
def bst_data():
    data = [50, 30, 20, 40, 70, 60, 80]
    return data


@pytest.fixture()
def traversal_data():
    data = [6, 4, 9, 2, 5, 8, 12]
    return data


def test_insert(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert(n)

    assert bst.search(20) == True
    assert bst.search(25) == False


def test_search(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert(n)

    assert bst.search(20) == True
    assert bst.search(25) == False


def test_dfs(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert(n)

    assert bst.bfs(bst.root) == [[50], [30, 70], [20, 40, 60, 80]]


def test_search_iter(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert(n)

    assert bst.search_iter(20) == True
    assert bst.search_iter(25) == False


def test_traversals_reset(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert(n)

    assert bst.in_order_traversal(bst.root) == [20, 30, 40, 50, 60, 70, 80]
    assert bst.pre_order_traversal(bst.root) == [50, 30, 20, 40, 70, 60, 80]
    assert bst.post_order_traversal(bst.root) == [20, 40, 30, 60, 80, 70, 50]


def test_find_closest_value(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert_iter(n)

    assert bst.find_closest_value(31) == 30


def test_remove_root(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert_iter(n)

    bst.remove(50)
    assert bst.search_iter(50) is False
    assert bst.bfs(bst.root) == [[60], [30, 70], [20, 40, 80]]


def test_validate_bst(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert_iter(n)
    assert bst.validate_bst() == True


def test_in_order_traversal(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.in_order_traversal(bst.root) == sorted(traversal_data)


def test_pre_order_traversal(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.pre_order_traversal(bst.root) == [6, 4, 2, 5, 9, 8, 12]


def test_post_order_traversal(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.post_order_traversal(bst.root) == [2, 5, 4, 8, 12, 9, 6]


def test_in_order_iterative(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.in_order_iterative(bst.root) == sorted(traversal_data)


def test_pre_order_iterative(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.pre_order_iterative(bst.root) == [6, 4, 2, 5, 9, 8, 12]


def test_post_order_iterative(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.post_order_iterative(bst.root) == [2, 5, 4, 8, 12, 9, 6]


def test_create_min_height_bst():
    bst = BST()
    data = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    node = bst.create_min_height_bst(data)
    res = bst.bfs(node)
    assert res == [[10], [2, 14], [1, 5, 13, 15], [7, 22]]


def test_kth_largest(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.kth_largest(bst.root, 3) == 8
    assert bst.kth_largest(bst.root, 1) == 12
