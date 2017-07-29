# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        elif t2:
            t1 = t2

        return t1

root1 = TreeNode(1)
left1 = TreeNode(3)
right1 = TreeNode(2)
root1.left = left1
root1.right = right1

root2 = TreeNode(2)
left2 = TreeNode(1)
right2 = TreeNode(3)
root2.left = left2
root2.right = right2

root = Solution().mergeTrees(root1, root2)
assert root.val == 3
assert root.left.val == 4
assert root.right.val == 5