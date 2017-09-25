class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.vals = []
        def traverse(root):
            if root:
                traverse(root.left)
                self.vals.append(root.val)
                traverse(root.right)

        traverse(root)

        i = 0
        j = len(self.vals) - 1
        while i < j:
            if self.vals[i] + self.vals[j] == k:
                return True
            elif self.vals[i] + self.vals[j] > k:
                j -= 1
            else:
                i += 1
        return False

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

assert Solution().findTarget(root, 9) == True
assert Solution().findTarget(root, 28) == False