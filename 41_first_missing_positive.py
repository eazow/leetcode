class Solution(object):
    def firstMissingPositive(self, nums):
        """"
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        last_num = 0
        for num in nums:
            if num <= 0:
                continue
            if num - last_num > 1:
                return last_num + 1
            last_num = num

        return last_num + 1


assert Solution().firstMissingPositive([1, 2, 0]) == 3
assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2
assert Solution().firstMissingPositive([7, 8, 9, 10, 11, 12]) == 1
