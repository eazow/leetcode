import copy

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsetsList = [[]]
        for num in nums:
            tmpLists = copy.deepcopy(subsetsList)
            for tmpList in tmpLists:
                tmpList.append(num)
                subsetsList.append(tmpList)
        return subsetsList


nums = [1,2,3]
print Solution().subsets(nums)
