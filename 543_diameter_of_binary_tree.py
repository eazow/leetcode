class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def depth(node):
            if node:
                l_depth = depth(node.left)
                r_depth = depth(node.right)
                self.diameter = max(self.diameter, l_depth + r_depth)
                return max(l_depth, r_depth) + 1
            return 0

        depth(root)
        return self.diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
assert Solution().diameterOfBinaryTree(root) == 3