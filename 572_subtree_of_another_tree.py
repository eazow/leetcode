class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        def traverse(root):
            if root:
                self.nodes += "%s," % root.val
                traverse(root.left)
                traverse(root.right)
            else:
                self.nodes += "#,"
            return self.nodes

        self.nodes = ","
        tree_s = traverse(s)
        self.nodes = ","
        tree_t = traverse(t)
        if tree_s.find(tree_t) > -1:
            return True
        return False

s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)
assert Solution().isSubtree(s, t) == True

s.left.right.left = TreeNode(0)
assert Solution().isSubtree(s, t) == False

s = TreeNode(12)
t = TreeNode(2)
assert Solution().isSubtree(s, t) == False