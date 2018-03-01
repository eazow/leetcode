class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low < high:
            middle = (low + high) / 2

            if middle % 2 == 1:
                middle -= 1
            if nums[middle] == nums[middle + 1]:
                low = middle + 2
            else:
                high = middle

        return nums[low]

assert Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
assert Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10