class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.find_paths_from_node(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def find_paths_from_node(self, node, sum):
        if not node:
            return 0
        if node.val == sum:
            return 1 + self.find_paths_from_node(node.left, sum - node.val) \
                   + self.find_paths_from_node(node.right, sum - node.val)

        return self.find_paths_from_node(node.left, sum - node.val) \
               + self.find_paths_from_node(node.right, sum - node.val)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

assert Solution().pathSum(root, 8) == 3
assert Solution().pathSum(root, -2) == 1