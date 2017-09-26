class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        last = nums[0]
        i = 1
        result = 1
        length = 1
        while i < len(nums):
            num = nums[i]
            if num > last:
                length += 1
                last = num
                result = max(length, result)
            else:
                result = max(length, result)
                last = num
                length = 1
            i += 1
        return result

assert Solution().findLengthOfLCIS([1, 3, 5, 4, 7]) == 3
assert Solution().findLengthOfLCIS([2, 2, 2, 2, 2]) == 1
assert Solution().findLengthOfLCIS([1, 3, 5, 7, 9]) == 5