class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: int
        """
        nums = sorted(nums)
        closest = float("inf")
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    return target

        return closest


assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
assert Solution().threeSumClosest([-3, 0, 1, 2], 1) == 0
assert Solution().threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82) == 82
