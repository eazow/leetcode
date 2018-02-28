class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        node = None
        if nums:
            max_num = max(nums)
            max_index = nums.index(max_num)
            node = TreeNode(max_num)
            node.left = self.constructMaximumBinaryTree(nums[:max_index])
            node.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return node

nums = [3, 2, 1, 6, 0, 5]
root = Solution().constructMaximumBinaryTree(nums)
assert root.val == 6
assert root.left.val == 3
assert root.left.right.val == 2
assert root.left.right.right.val == 1
assert root.right.val == 5
assert root.right.left.val == 0