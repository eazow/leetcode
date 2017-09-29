class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.last = None
        self.max_count = 0
        self.last_count = 0
        def get_max_count(node):
            if node:
                get_max_count(node.left)
                if node.val == self.last:
                    self.last_count += 1
                else:
                    self.last = node.val
                    self.last_count = 1
                self.max_count = max(self.max_count, self.last_count)
                get_max_count(node.right)
        get_max_count(root)

        self.last = None
        self.last_count = 0
        self.modes = []
        def get_modes(node):
            if node:
                get_modes(node.left)
                if node.val == self.last:
                    self.last_count += 1
                else:
                    self.last = node.val
                    self.last_count = 1
                if self.last_count == self.max_count:
                    self.modes.append(node.val)
                get_modes(node.right)

        get_modes(root)
        return self.modes

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

assert Solution().findMode(root) == [2]
