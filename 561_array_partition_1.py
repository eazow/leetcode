class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        sum = 0
        while i < len(nums):
            sum += nums[i]
            i += 2
        return sum

assert Solution().arrayPairSum([1,4,3,2])==4