# -*- coding:utf-8 -*-

class Solution(object):
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        """
        1. 先从右往左遍历，找到nums[i] < nums[i+1]的节点nums[i]，将i记为left
        2. 从右往左遍历，找到第一个大于nums[left]的节点nums[i]，将i记为right
        3. 交换nums[left], nums[right]
        4. 将nums[right:]倒序
        :param nums: List[int]
        :return: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return

        i = len(nums) - 1
        while nums[i - 1] > nums[i]:
            i -= 1
        left = i - 1

        if left >= 0:
            i = len(nums) - 1
            while nums[i] <= nums[left] and i > left:
                i -= 1
            right = i
            nums[left], nums[right] = nums[right], nums[left]

        self.reverse(nums, left+1, len(nums)-1)


# nums = [1,2,7,5,3,1]
# Solution().nextPermutation(nums)
# assert nums == [1,3,1,2,5,7]
#
# nums = [1,2,3]
# Solution().nextPermutation(nums)
# assert nums == [1,3,2]

# nums = [1,5,1]
# Solution().nextPermutation(nums)
# assert nums == [5,1,1]

# Solution().nextPermutation([1, 1])

# Solution().nextPermutation([1, 1])

Solution().nextPermutation([3, 2, 1])
# Solution().nextPermutation([1,2,3]) == [1,3,2]
