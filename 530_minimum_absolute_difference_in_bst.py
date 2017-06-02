import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.minValue = sys.maxint
        self.list = []

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.minValue


    def traverse(self, node):
        if node.left:
            self.traverse(node.left)
        if self.list:
            self.minValue = min(self.minValue, node.val-self.list.pop())
        self.list.append(node.val)
        if node.right:
            self.traverse(node.right)

root = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(2)
assert Solution().getMinimumDifference(root) == 1