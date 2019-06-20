# -*- coding:utf-8 -*-
import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :param root: TreeNode
        :return: bool
        """
        return self.dfs(root, -sys.maxint, sys.maxint)

    def dfs(self, node, min_value, max_value):
        if node:
            if node.val <= min_value or node.val >= max_value:
                return False
            return self.dfs(node.left, min_value, node.val) \
                and self.dfs(node.right, node.val, max_value)
        return True


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
assert Solution().isValidBST(root) is False

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert Solution().isValidBST(root) is True

root = TreeNode(1)
root.left = TreeNode(1)
assert Solution().isValidBST(root) is False
