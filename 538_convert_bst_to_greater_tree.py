class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.basic = 0

    def convertBST(self, root):
        if root:
            self.traverse(root)
        return root

    def traverse(self, node):
        if node.right:
            self.traverse(node.right)

        self.basic += node.val
        node.val = self.basic

        if node.left:
            self.traverse(node.left)

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

root = Solution().convertBST(root)
assert root.val == 18
assert root.left.val == 20