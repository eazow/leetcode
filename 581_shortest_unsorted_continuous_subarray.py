class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        start = 0
        while start < len(nums):
            if sorted_nums[start] != nums[start]:
                break
            else:
                start += 1

        end = len(nums) - 1
        while end >= start:
            if sorted_nums[end] != nums[end]:
                break
            else:
                end -= 1
        return end - start + 1

assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
assert Solution().findUnsortedSubarray([1, 2, 3, 4]) == 0