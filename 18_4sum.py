class Solution():
    def fourSum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[List[int]]
        """
        nums.sort()
        result = []
        result_set = set()
        for left in xrange(len(nums) - 3):
            for right in xrange(len(nums) - 1, 2, -1):
                i = left + 1
                j = right - 1
                while i < j:
                    the_sum = nums[left] + nums[i] + nums[j] + nums[right]
                    if the_sum == target:
                        key = "%s_%s_%s_%s" % (nums[left], nums[i], nums[j], nums[right])
                        if key not in result_set:
                            result.append([nums[left], nums[i], nums[j], nums[right]])
                            result_set.add(key)
                        i += 1
                        j -= 1
                    elif the_sum > target:
                        j -= 1
                    else:
                        i += 1

        return result


assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
assert Solution().fourSum([-5, 5, 4, -3, 0, 0, 4, -2], 4) == [[-5, 0, 4, 5], [-3, -2, 4, 5]]
