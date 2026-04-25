from structures.stack import Stack


def test_stack():
    s = Stack()
    s.push(6)
    s.push(4)
    s.push(5)
    s.push(7)
    s.push(8)
    assert s.push(0) == False
    assert s.peek() == 8
    assert s.pop() == 8
    assert s.size() == 4
    assert s.peek() == 7
    assert s.pop() == 7
    assert s.pop() == 5
    assert s.pop() == 4
    assert s.pop() == 6
    assert s.pop() == -1
    assert s.peek() == -1
