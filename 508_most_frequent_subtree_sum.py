import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.counter = collections.Counter()
        self.postOrderTraverse(root)
        maxValue = max(self.counter.values())

        return [key for key in self.counter.keys() if self.counter[key] == maxValue]


    def postOrderTraverse(self, node):
        if node.left:
            node.val += self.postOrderTraverse(node.left)
        if node.right:
            node.val += self.postOrderTraverse(node.right)

        self.counter[node.val] += 1
        return node.val


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)
assert Solution().findFrequentTreeSum(root) == [2, 4, -3]

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
assert Solution().findFrequentTreeSum(root) == [2]