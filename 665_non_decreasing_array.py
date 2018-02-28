class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        count = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i + 1]:
                count += 1
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
            if count > 1:
                return False
            i += 1
        return True

assert Solution().checkPossibility([3, 4, 2, 5, 6]) == True
assert Solution().checkPossibility([1, 4, 2, 5, 6]) == True
assert Solution().checkPossibility([3, 4, 2, 3]) == False
