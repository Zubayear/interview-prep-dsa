import collections


class Node:
  def __init__(self, key):
    self.val = key
    self.right = self.left = None


class BST:
  def __init__(self):
    self.root = None

  def insert(self, key):
    if self.root is None:
      self.root = Node(key)
    else:
      self._insert(self.root, key)

  def _insert(self, node, key):
    if key < node.val:
      if node.left is None:
        node.left = Node(key)
      else:
        self._insert(node.left, key)
    else:
      if node.right is None:
        node.right = Node(key)
      else:
        self._insert(node.right, key)

  def search(self, key):
    if self.root is None:
      return False
    return self._search(self.root, key)

  def _search(self, node, key):
    if node is None:
      return False
    if node.val == key:
      return True
    if node.val > key:
      return self._search(node.left, key)
    return self._search(node.right, key)

  def bfs(self, root=None):
    if root is None:
      root = self.root
    if root is None:
      return []
    queue = collections.deque([root])
    res = []
    while queue:
      size = len(queue)
      tmp = []
      for _ in range(size):
        cur_node = queue.popleft()
        tmp.append(cur_node.val)
        if cur_node.left is not None:
          queue.append(cur_node.left)
        if cur_node.right is not None:
          queue.append(cur_node.right)
      res.append(tmp)
    return res

  def search_iter(self, key):
    cur_node = self.root
    while cur_node is not None:
      if key == cur_node.val:
        return True
      if cur_node.val > key:
        cur_node = cur_node.left
      else:
        cur_node = cur_node.right
    return False

  def insert_iter(self, key):
    current = Node(key)
    if self.root is None:
      self.root = current
      return
    current = self.root
    while True:
      if current.val > key:
        if current.left is None:
          current.left = Node(key)
          break
        current = current.left
      else:
        if current.right is None:
          current.right = Node(key)
          break
        current = current.right

  def in_order_traversal(self, root):
    result = []
    def helper(node):
      if node is None:
        return
      helper(node.left)
      result.append(node.val)
      helper(node.right)
    helper(root)
    return result

  def inorder_traversal(self, root):
    return self.in_order_traversal(root)

  def pre_order_traversal(self, root):
    result = []
    def helper(node):
      if node is None:
        return
      result.append(node.val)
      helper(node.left)
      helper(node.right)
    helper(root)
    return result

  def post_order_traversal(self, root):
    result = []
    def helper(node):
      if node is None:
        return
      helper(node.left)
      helper(node.right)
      result.append(node.val)
    helper(root)
    return result

  def remove(self, key):
    self.root = self._remove(self.root, key)

  def _remove(self, node, key):
    if node is None:
      return None
    if key < node.val:
      node.left = self._remove(node.left, key)
      return node
    if key > node.val:
      node.right = self._remove(node.right, key)
      return node
    if node.left is None:
      return node.right
    if node.right is None:
      return node.left
    successor_val = self.get_successor(node.right)
    node.val = successor_val
    node.right = self._remove(node.right, successor_val)
    return node

  def get_successor(self, node):
    current_node = node
    while current_node.left is not None:
      current_node = current_node.left
    return current_node.val

  def find_closest_value(self, key):
    if self.root is None:
      return None
    if self.root.val == key:
      return key
    closest = self.root.val
    current_node = self.root
    while current_node is not None:
      if abs(closest - key) > abs(current_node.val - key):
        closest = current_node.val
      if current_node.val < key:
        current_node = current_node.right
      else:
        current_node = current_node.left
    return closest

  def validate_bst(self):
    if self.root is None:
      return True
    return self._validate_bst(self.root, float("-inf"), float("inf"))

  def _validate_bst(self, node, min_val, max_val):
    if node is None:
      return True
    if node.val < min_val or node.val > max_val:
      return False
    return self._validate_bst(node.left, min_val, node.val) and self._validate_bst(node.right, node.val, max_val)

  def in_order_iterative(self, root):
    stack = collections.deque()
    result = []
    if root is None:
      return result
    current_node = root
    while True:
      while current_node is not None:
        stack.appendleft(current_node)
        current_node = current_node.left
      if len(stack) == 0:
        break
      current_node = stack.popleft()
      result.append(current_node.val)
      current_node = current_node.right
    return result

  def pre_order_iterative(self, root):
    stack = collections.deque()
    result = []
    if root is None:
      return result
    stack.appendleft(root)
    while stack:
      current_node = stack.popleft()
      result.append(current_node.val)
      if current_node.right:
        stack.appendleft(current_node.right)
      if current_node.left:
        stack.appendleft(current_node.left)
    return result

  def post_order_iterative(self, root):
    stack = collections.deque()
    result = []
    if root is None:
      return result
    stack.appendleft(root)
    while stack:
      node = stack.popleft()
      result.append(node.val)
      if node.left:
        stack.appendleft(node.left)
      if node.right:
        stack.appendleft(node.right)
    return result[::-1]

  def create_min_height_bst(self, arr):
    if arr is None or len(arr) == 0:
      return None
    return self._create_min_height_bst(arr, 0, len(arr) - 1)

  def _create_min_height_bst(self, arr, start, end):
    if start > end:
      return None
    mid = (start + end) // 2
    node = Node(arr[mid])
    node.left = self._create_min_height_bst(arr, start, mid - 1)
    node.right = self._create_min_height_bst(arr, mid + 1, end)
    return node

  def kth_largest(self, root, k):
    stack = collections.deque()
    n = 0
    if root is None:
      return -1
    current_node = root
    while True:
      while current_node is not None:
        stack.appendleft(current_node)
        current_node = current_node.right
      if len(stack) == 0:
        break
      current_node = stack.popleft()
      n += 1
      if n == k:
        return current_node.val
      current_node = current_node.left
    return -1

  def reconstruct_bst(self, arr):
    if arr is None or len(arr) == 0:
      return None
    root = Node(arr[0])
    idx = 1
    while idx < len(arr) and arr[idx] < root.val:
      idx += 1
    root.left = self.reconstruct_bst(arr[1:idx])
    root.right = self.reconstruct_bst(arr[idx:])
    return root
