class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.traverse(root)
        return self.result

    def traverse(self, node):
        if node:
            self.traverse(node.left)
            self.traverse(node.right)

            if node.left and node.right:
                self.result += abs(node.right.val - node.left.val)
                node.val += node.right.val + node.left.val
            elif node.left:
                self.result += abs(node.left.val)
                node.val += node.left.val
            elif node.right:
                self.result += abs(node.right.val)
                node.val += node.right.val

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
assert Solution().findTilt(root) == 7

root = TreeNode(-8)
root.left = TreeNode(3)
root.right = TreeNode(0)
root.left.left = TreeNode(-8)
root.left.left.right = TreeNode(-1)
root.left.left.right.right = TreeNode(8)
assert Solution().findTilt(root) == 18