import collections


class Node:
    def __init__(self, key):
        self.val = key
        self.right = self.left = None


class BST:
    def __init__(self):
        self.root = None
        self.res = []

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

    def bfs(self, root):
        queue = collections.deque()
        queue.append(root)
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
        print(res)
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

    def inOrder_traversal(self, root):
        """
        visit the left subtree, then the root node, and finally the right subtree.
        """
        if root is None:
            return self.res
        self.inOrder_traversal(root.left)
        self.res.append(root.val)
        self.inOrder_traversal(root.right)
        return self.res

    def preOrder_traversal(self, root):
        """
        visit the root node, then the left subtree, and finally the right subtree.
        """
        if root is None:
            return self.res
        self.res.append(root.val)
        self.preOrder_traversal(root.left)
        self.preOrder_traversal(root.right)
        return self.res

    def postOrder_traversal(self, root):
        """
        visit the left subtree, then the right subtree, and finally the root node
        """
        if root is None:
            return self.res
        self.postOrder_traversal(root.left)
        self.postOrder_traversal(root.right)
        self.res.append(root.val)
        return self.res

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

    def inOrder_iterative(self, root):
        stack = collections.deque()
        result = []
        if root is None:
            return result

        # Start with root node
        current_node = root

        while True:
            # Go left as far as possible and push nodes onto stack
            while current_node is not None:
                stack.appendleft(current_node)
                current_node = current_node.left

            if len(stack) == 0:
                break

            # Pop the top node from the stack and visit it
            # [2,4,6] stack
            current_node = stack.popleft()
            result.append(current_node.val)

            # Move to the right child if it exists
            current_node = current_node.right
        return result

    def preOrder_iterative(self, root):
        """
        1. Initialize an empty stack and push the root node onto the stack.
        2. While the stack is not empty, pop the top node from the stack and visit it.
        3. Push the right child of the current node onto the stack if it exists.
        4. Push the left child of the current node onto the stack if it exists.

        we push its right child (if it exists) onto the stack first and then its left child (if it exists).
        This ensures that the left child of the current node is visited before its right child
        """
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

    def postOrder_iterative(self, root):
        """
        1. Initialize an empty stack and push the root node onto the stack.
        2. While the stack is not empty, pop the top node from the stack and add its value to the result list.
        3. Push the left child of the current node onto the stack if it exists.
        4. Push the right child of the current node onto the stack if it exists.
        5. Reverse the result list to get the post-order traversal of the binary tree.

        When we have visited all the nodes, the result list will contain the nodes in reverse order of a post-order traversal. 
        Therefore, we need to reverse the result list to get the actual post-order traversal of the binary tree.
        """
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
        """
        reverse inOrder => right, visit, left
        """
        stack = collections.deque()
        n = 0
        if root is None:
            return -1
        current_node = root
        while True:
            while current_node is not None:
                # go all the way to right
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
