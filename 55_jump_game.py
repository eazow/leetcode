class Solution(object):
    def canJump(self, nums):
        """
        :param nums: List[int]
        :return: boolean
        """
        if len(nums) == 0:
            return True
        return self.jump(nums, 0, 0)

    def jump(self, nums, start, end):
        new_end = end
        new_start = start
        for i in range(start, end+1):
            step = nums[i]
            if start + step >= len(nums) - 1:
                return True
            elif step == 0:
                continue
            elif start + step > new_end:
                new_end = start + step

        if new_end > start:
            new_start = start + 1

        if new_start == new_end and nums[new_start] == 0:
            return False
        return self.jump(nums, new_start, new_end)


assert Solution().canJump([2, 3, 1, 1, 4]) is True
assert Solution().canJump([3, 2, 1, 0, 4]) is False
assert Solution().canJump([]) is True
assert Solution().canJump([0]) is True
