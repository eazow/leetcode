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
        sum_n_array = []
        def dfs(node, level):
            if node:
                if len(sum_n_array) <= level:
                    sum_n_array.append([0,0])

                sum_n_array[level][0] += node.val
                sum_n_array[level][1] += 1

                dfs(node.left, level+1)
                dfs(node.right, level+1)

        dfs(root, 0)

        result = []
        for sum_n in sum_n_array:
            result.append(sum_n[0]/float(sum_n[1]))

        return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

assert Solution().averageOfLevels(root) == [3, 14.5, 11]