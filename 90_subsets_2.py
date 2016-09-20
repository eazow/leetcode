class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        i = 0
        resultSize = 0
        while i < len(nums):
            num = nums[i]
            resultIndex = 0
            if i>0 and nums[i]==nums[i-1]:
                resultIndex = resultSize;
            resultSize = len(result)
            while resultIndex < resultSize:
                tempList = result[resultIndex][:]
                tempList.append(num)
                result.append(tempList)
                resultIndex += 1
            i += 1
        return result

assert Solution().subsetsWithDup([1,2,2]) == [[],[1],[2],[1,2],[2,2],[1,2,2]]
