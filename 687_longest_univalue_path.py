class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode:
        :rtype: int
        """
        self.longest = 0

        def get_depth(node):
            """
            获取节点的深度
            """
            if node == None:
                return 0
            left = get_depth(node.left)
            right = get_depth(node.right)

            left_with_root = 0
            if node.left and node.val == node.left.val:
                left_with_root = left + 1
            right_with_root = 0
            if node.right and node.val == node.right.val:
                right_with_root = right + 1
            self.longest = max(self.longest, left_with_root + right_with_root)

            return max(left_with_root, right_with_root)

        get_depth(root)
        return self.longest

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)
assert Solution().longestUnivaluePath(root) == 2

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)
assert Solution().longestUnivaluePath(root) == 2