class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])

assert Solution().maximumProduct([1,2,3,4]) == 24
assert Solution().maximumProduct([-4,-3,-2,-1,60]) == 720