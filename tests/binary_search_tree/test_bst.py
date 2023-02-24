from binary_search_tree.bst import BST


def test_insert():
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    assert bst.search(20) == True
    assert bst.search(25) == False

def test_search():
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    assert bst.search(20) == True
    assert bst.search(25) == False

def test_dfs():
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    res = bst.bfs()
    print(res)

def test_search_iter():
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    # bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    # bst.insert(80)

    assert bst.search_iter(20) == True
    assert bst.search_iter(25) == False

def test_search_iter():
    bst = BST()
    bst.insert_iter(50)
    bst.insert_iter(30)
    bst.insert_iter(20)
    bst.insert_iter(40)
    bst.insert_iter(70)
    bst.insert_iter(60)
    bst.insert_iter(80)

    # assert bst.bfs() == [[50], [30, 70], [20, 40, 60, 80]]
    # assert bst.search_iter(20) == True
    # assert bst.search_iter(25) == False
    # bst.inorder_traversal(bst.root)

def test_remove():
    bst = BST()
    bst.insert_iter(50)
    bst.insert_iter(30)
    bst.insert_iter(20)
    bst.insert_iter(40)
    bst.insert_iter(70)
    bst.insert_iter(60)
    bst.insert_iter(80)

    # assert bst.bfs() == [[50], [30, 70], [20, 40, 60, 80]]
    # assert bst.search_iter(20) == True
    # assert bst.search_iter(25) == False
    # bst.inorder_traversal(bst.root)
    bst.remove(50)
    print("------")
    bst.inorder_traversal(bst.root)
    # assert bst.search_iter(40) == False