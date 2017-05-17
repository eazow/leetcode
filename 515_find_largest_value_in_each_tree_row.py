class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = self.traverse(root, 0, {})
        values = []
        for key in result:
            values.append(result[key])
        return values

    def traverse(self, root, depth, result):
        if not root:
            return []
        if (not result.has_key(depth)) or (result[depth] < root.val):
            result[depth] = root.val
        if root.left:
            result = self.traverse(root.left, depth+1, result)
        if root.right:
            result = self.traverse(root.right, depth+1, result)
        return result


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)


assert Solution().largestValues(root) == [1,3,9]
assert Solution().largestValues(None) == []