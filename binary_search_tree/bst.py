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
            # this is the root
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            # go to left
            if node.left is None:
                # this is the left node
                node.left = Node(key)
            else:
                # otherwise recursively add the key to left side
                self._insert(node.left, key)
        else:
            # go to right
            if node.right is None:
                # if there is no right node then this is the right node
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
            # go to left
            return self._search(node.left, key)
        if node.val < key:
            # go to right
            return self._search(node.right, key)

    def bfs(self):
        queue = collections.deque()
        queue.append(self.root)
        res = []
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
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
        # very first key is root
        current = Node(key)
        if self.root is None:
            # if root is None we will face issue
            self.root = current
            return
        current = self.root
        while True:
            if current.val > key:
                # go to left
                if current.left is None:
                    # this is the end so add key as node
                    current.left = Node(key)
                    break
                else:
                    # explore left
                    current = current.left
            else:
                # go to right
                if current.right is None:
                    current.right = Node(key)
                    break
                else:
                    current = current.right

    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.val)
        self.inorder_traversal(root.right)

    def remove(self, key):
        self._remove(self.root, key)

    def _remove(self, node, key, parent_node=None):
        current_node = node
        while current_node is not None:
            if current_node.val > key:
                """
                    30 current_node, parent_node
                    /
                   20 parent_node
                  /
                 10 current_node
                """
                parent_node = current_node
                # go to left
                current_node = current_node.left
            elif current_node.val < key:
                parent_node = current_node
                # go to right
                current_node = current_node.right
            else:
                # found the node
                # 2 child case
                if current_node.left is not None and current_node.right is not None:
                    # get successor and set its value to current_node val
                    # we're getting the left most value in right subtree
                    current_node.val = self.get_successor(current_node.right)
                    self._remove(current_node, current_node.right.val)

                # either only one child or none
                elif parent_node is None:  # root node have no parent
                    # we're sure there is only one child or none
                    if current_node.left is not None:
                        # """
                        #     30 current_node
                        #     / \
                        #    20
                        #   / |
                        #  10 25
                        #  replace left subtree with 30
                        # """
                        current_node.key = current_node.left.key
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.key = current_node.right.key
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        current_node.key = None
                # check is our current_node itself a left child or right child
                elif parent_node.left == current_node:
                    """
                        30 
                        /
                       20 parent_node
                      /
                     10 current_node
                    /
                   2  
                    """
                    # attach 2 to 20
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    # """
                    #     30
                    #     /
                    #    20 parent_node
                    #     \
                    #     10 current_node
                    #     /
                    #    2
                    # """
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break

    def get_successor(self, node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.val

    def find_closest_value(self, key):
        if self.root is None:
            return
        if self.root.val == key:
            return key
        closest = float("inf")
        current_node = self.root
        """
        |closest - key| < |current_node - key|
        update closest based on this condition
        """
        while current_node is not None:
            if current_node.val == key:
                closest = current_node.val
                break
            if abs(closest - key) < abs(current_node.val - key):
                continue
            else:
                closest = current_node.val
            # go to left or right
            if current_node.val < key:
                # go to right
                current_node = current_node.right
            else:
                current_node = current_node.left
        return closest

    def validate_bst(self):
        if self.root is None:
            return True
        # root node's limit is -inf < root < inf
        return self._validate_bst(self.root, float("-inf"), float("inf"))

    def _validate_bst(self, node, min_val, max_val):
        # leaf node or null tree
        if node is None:
            return True
        # bst property
        # node's value between min_val and max_val for wrapping
        if node.val < min_val or node.val > max_val:
            return False
        # for left: max_val is root of x
        # for right: min_val is root of x
        # so when going left keep the min_val same update max_val to node val
        # and when going right keep the max_val same and update min_val to node val
        left_is_valid = self._validate_bst(node.left, min_val, node.val)
        right_is_valid = self._validate_bst(node.right, node.val, max_val)
        return left_is_valid and right_is_valid
