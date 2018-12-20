class Solution(object):
    def search(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            middle = (low + high) / 2
            if nums[middle] == target:
                return middle

            # 左半段有序, 类似[4, 5, 6, 7, 8, 0, 1, 2]，注意需要加上nums[middle] == nums[low]的条件
            if nums[middle] >= nums[low]:
                if nums[low] <= target < nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            # 右半段有序，类似[4, 5, 6, 0, 1, 2, 3]
            else:
                if nums[middle] < target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1

        return -1


# print Solution().search([1, 2, 3, 4, 5, 6, 7], 1)
# print Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
print Solution().search([5, 1, 2, 3, 4], 1)

# print Solution().search([4, 5, 6, 7, 0, 1, 2], 0)