class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.result = 0
        self.traverse(root)
        return self.result

    def traverse(self, node, isLeft=False):
        if node and node.left == None and node.right == None and isLeft:
            self.result += node.val
        if node:
            self.traverse(node.left, True)
            self.traverse(node.right)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

assert Solution().sumOfLeftLeaves(root) == 24