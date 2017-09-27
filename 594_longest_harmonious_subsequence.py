class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1

        result = 0
        for num in nums_count:
            count = nums_count[num]
            if nums_count.get(num+1):
                result = max(result, count + nums_count[num+1])
        return result

assert Solution().findLHS([1,3,2,2,5,2,3,7]) == 5