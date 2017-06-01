import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.minValue = sys.maxint

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.minValue


    def traverse(self, node):
        if node.left:
            self.minValue = min(self.minValue, node.val-node.left.val)
            self.traverse(node.left)
        if node.right:
            self.minValue = min(self.minValue, node.right.val-node.val)
            self.traverse(node.right)

root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
assert Solution().getMinimumDifference(root) == 1