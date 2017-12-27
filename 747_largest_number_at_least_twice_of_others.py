import sys

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0 - sys.maxint
        second = 0 - sys.maxint
        i = 0
        first_index = 0
        for num in nums:
            if num > first:
                second = first
                first = num
                first_index = i
            elif num > second:
                second = num

            i += 1

        if second * 2 <= first:
            return first_index
        return -1

assert Solution().dominantIndex([3, 6, 1, 0]) == 1
assert Solution().dominantIndex([0, 0, 3, 2]) == -1