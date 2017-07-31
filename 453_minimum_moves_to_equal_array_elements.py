class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum(nums) - len(nums) * nums[0]

assert Solution().minMoves([1,2,3]) == 3
assert Solution().minMoves([1,1,3]) == 2