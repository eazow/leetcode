class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        sort(nums)
        i = 0
        while i < len(nums):
            num = nums[i]
             
