import pytest

from binary_search_tree.bst import BST


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

    res = bst.bfs()
    print(res)


def test_search_iter(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert(n)

    assert bst.search_iter(20) == True
    assert bst.search_iter(25) == False


def test_search_iter(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert(n)

    assert bst.bfs() == [[50], [30, 70], [20, 40, 60, 80]]
    assert bst.search_iter(20) == True
    assert bst.search_iter(25) == False
    bst.inorder_traversal(bst.root)


# def test_remove():
#     bst = BST()
#     bst.insert_iter(50)
#     bst.insert_iter(30)
#     bst.insert_iter(20)
#     bst.insert_iter(40)
#     bst.insert_iter(70)
#     bst.insert_iter(60)
#     bst.insert_iter(80)

    # assert bst.bfs() == [[50], [30, 70], [20, 40, 60, 80]]
    # assert bst.search_iter(20) == True
    # assert bst.search_iter(25) == False
    # bst.inorder_traversal(bst.root)
    # bst.remove(50)
    # print("------")
    # bst.inorder_traversal(bst.root)
    # assert bst.search_iter(40) == False


def test_find_closest_value(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert_iter(n)

    assert bst.find_closest_value(31) == 30


def test_validate_bst(bst_data):
    bst = BST()
    for n in bst_data:
        bst.insert_iter(n)
    assert bst.validate_bst() == True


def test_inOrder_traversal(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.inOrder_traversal(bst.root) == sorted(traversal_data)


def test_preOrder_traversal(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.preOrder_traversal(bst.root) == [6, 4, 2, 5, 9, 8, 12]


def test_postOrder_traversal(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.postOrder_traversal(bst.root) == [2, 5, 4, 8, 12, 9, 6]


def test_inOrder_iterative(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.inOrder_iterative(bst.root) == sorted(traversal_data)


def test_preOrder_iterative(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.preOrder_iterative(bst.root) == [6, 4, 2, 5, 9, 8, 12]


def test_postOrder_iterative(traversal_data):
    bst = BST()
    for n in traversal_data:
        bst.insert_iter(n)
    assert bst.postOrder_iterative(bst.root) == [2, 5, 4, 8, 12, 9, 6]
