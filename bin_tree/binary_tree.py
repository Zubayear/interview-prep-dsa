from typing import Optional

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def __repr__(self):
    return f"Node({self.data})"

class BinaryTree:
  def __init__(self, root=None):
    self.root = root

  def insert(self, data: Optional[TreeNode]):
    # Level by level insert
    new_node = TreeNode(data)
    if self.root is None:
      self.root = new_node
      return

    queue = [self.root]
    while queue:
      node = queue.pop(0)
      if node.left is None:
        node.left = new_node
        return
      else:
        queue.append(node.left)

      if node.right is None:
        node.right = new_node
        return
      else:
        queue.append(node.right)

  def search(self, data: Optional[TreeNode]) -> bool:
    if self.root is None:
      return False
    queue = [self.root]

    while queue:
      node = queue.pop(0)
      if node.data == data:
        return True
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    return False