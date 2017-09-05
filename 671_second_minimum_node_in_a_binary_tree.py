import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        self.min = sys.maxint
        self.second_min = sys.maxint
        def traverse(node):
            if node:
                if node.val < self.min:
                    self.second_min = self.min
                    self.min = node.val
                elif node.val < self.second_min and node.val != self.min:
                    self.second_min = node.val

                traverse(node.left)
                traverse(node.right)

        traverse(root)
        if self.second_min != sys.maxint:
            return self.second_min
        return -1

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

assert Solution().findSecondMinimumValue(root) == 5