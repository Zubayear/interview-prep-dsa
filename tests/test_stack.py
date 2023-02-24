from ds_impl import stack

def test_stack():
    s = stack.Stack()
    s.push(6)
    s.push(4)
    s.push(5)
    s.push(7)
    s.push(8)
    assert s.push(0) == False
    assert s.size() == 5