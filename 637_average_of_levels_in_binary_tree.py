class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        sums = []
        nums = []
        def dfs(node, level):
            if node:
                if len(sums) <= level:
                    sums.append(0)
                    nums.append(0)

                sums[level] += node.val
                nums[level] += 1

                dfs(node.left, level+1)
                dfs(node.right, level+1)

        dfs(root, 0)

        result = []
        for i in range(len(sums)):
            result.append(sums[i]/float(nums[i]))

        return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

assert Solution().averageOfLevels(root) == [3, 14.5, 11]