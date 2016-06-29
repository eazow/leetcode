class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        returnLists = [[]]
        for num in nums:
            newLists = []
            for returnList in returnLists:
                for i in range(len(returnList)+1):
                    newList = returnList[:i] + [num] + returnList[i:]
                    newLists.append(newList)
            returnLists = newLists
        return returnLists
        
assert Solution().permute([1,2,3])==[[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]