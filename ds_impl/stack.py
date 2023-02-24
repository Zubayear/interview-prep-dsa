class Stack:
    li = []
    top = -1
    def __init__(self) -> None:
        self.li = [0] * 5
    
    def push(self, val: int) -> bool:
        if self.is_full():
            return False
        self.top += 1
        self.li[self.top] = val
        return True
    
    def size(self) -> int:
        return self.top + 1

    def pop(self) -> int:
        if self.is_empty():
            return -1
        val = self.li[self.top]
        self.top -= 1
        return val
    
    def peek(self) -> int:
        if self.is_empty() or self.is_full():
            return -1
        return self.li[self.top]
    
    def is_empty(self) -> bool:
        return True if self.top == -1 else False
    
    def is_full(self) -> bool:
        return True if self.top + 1 == len(self.li) else False