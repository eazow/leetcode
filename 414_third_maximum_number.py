class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = None
        second = None
        third = None
        for num in nums:
            if first == None:
                first = num
            elif num > first:
                third = second
                second = first
                first = num
            elif num == first:
                continue
            elif second == None:
                second = num
            elif num > second:
                third = second
                second = num
            elif num == second:
                continue
            elif third == None or third < num:
                third = num

        return first if third == None else third

assert Solution().thirdMax([3, 2, 1]) == 1
assert Solution().thirdMax([1, 2]) == 2
assert Solution().thirdMax([2, 2, 3, 1]) == 1