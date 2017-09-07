class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        if root:
            if root.val == L:
                root.left = None
            elif root.val > L:
                root.left = self.trimBST(root.left, L, R)
            else:
                root = self.trimBST(root.right, L, R)
                return root

            if root.val == R:
                root.right = None
            elif root.val < R:
                root.right = self.trimBST(root.right, L, R)
            else:
                root = self.trimBST(root.left, L, R)

        return root

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)
assert Solution().trimBST(root, 3, 4) == None

root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root = Solution().trimBST(root, 1, 3)
assert root.val == 3
assert root.left.val == 2
assert root.right == None
assert root.left.left.val == 1