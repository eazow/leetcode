class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i]:
                cur += 1
            else:
                if cur > maxCount:
                    maxCount = cur
                cur = 0

        return max(cur, maxCount)

Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3