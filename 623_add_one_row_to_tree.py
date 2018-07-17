class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        def traverse(node, depth):
            if node:
                if depth == d - 1:
                    new_node1 = TreeNode(v)
                    left = node.left
                    node.left = new_node1
                    new_node1.left = left
                    new_node2 = TreeNode(v)
                    right = node.right
                    node.right = new_node2
                    new_node2.right = right
                traverse(node.left, depth + 1)
                traverse(node.right, depth + 1)

        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        traverse(root, 1)
        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left= TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)

root = Solution().addOneRow(root, 1, 2)
assert root.val == 4
assert root.left.val == 1
assert root.right.val == 1
assert root.left.left.val == 2
assert root.right.right.val == 6
assert root.left.left.left.val == 3
assert root.left.left.right.val == 1
assert root.right.right.left.val == 5
