class Solution(object):
    def threeSum(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        result = {}
        nums = sorted(nums)
        for i in range(len(nums)):
            j = len(nums) - 1
            while j > i + 1:
                k_start = i
                k_end = j
                k = (k_start + k_end) / 2
                while k_start <= k_end and i < k < j:
                    the_sum = nums[i] + nums[j] + nums[k]
                    if the_sum == 0:
                        result[nums[i], nums[k], nums[j]] = [nums[i], nums[j], nums[k]]
                        break
                    elif the_sum < 0:
                        k_start = k + 1
                    else:
                        k_end = k
                    k = (k_start + k_end) / 2
                    if k_start == k:
                        break
                j -= 1
        return result.values()


print Solution().threeSum([-1, 0, 1, 2, -1, -4])
print Solution().threeSum([1, 2, -2, -1])
print Solution().threeSum([-2, 0, 1, 1, 2])
