class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = ""

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t:
            self.result += str(t.val)
            if t.left or t.right:
                self.result += "("
            if t.left:
                self.tree2str(t.left)
            if t.left or t.right:
                self.result += ")"
            if t.right:
                self.result += "("
                self.tree2str(t.right)
                self.result += ")"
        
        return self.result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

assert Solution().tree2str(root) == "1(2(4))(3)"