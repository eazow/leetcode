class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for num in nums:
            tmpLists = subsets
            for tmpList in tmpLists:
                tmpList.add(num)

nums = [1,2,3]
Solution().subsets(nums)
