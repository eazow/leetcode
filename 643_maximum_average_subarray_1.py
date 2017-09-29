class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        sum = 0
        max_sum = 0
        while i < k and i < len(nums):
            sum += nums[i]
            i += 1
        max_sum = sum
        while i < len(nums):
            sum += nums[i] - nums[i-k]
            max_sum = max(sum, max_sum)
            i += 1

        return max_sum/float(k)

assert Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75