class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        if len(nums) == 0:
            return 0

        nums = sorted(nums)
        nums_set = set(nums)
        count = 0

        last = nums[0] - 1
        for i in nums:
            if i + k in nums_set and i != last:
                last = i
                count += 1
        if k != 0:
            return count
        else:
            same_count = len(nums) - len(nums_set)
            return min(count, same_count)

assert Solution().findPairs([3, 1, 4, 1, 5], 2) == 2
assert Solution().findPairs([1, 1, 1, 1, 1], 0) == 1
assert Solution().findPairs([1, 2, 3, 4, 5], 1) == 4
assert Solution().findPairs([1, 3, 1, 5, 4], 0) == 1
assert Solution().findPairs([1, 2, 3, 4, 5], -1) == 0