class Solution(object):
    def searchRange(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        left = 0
        right = len(nums) - 1
        hit = False
        result = []
        while left <= right:
            middle = (left + right) / 2
            if nums[middle] == target:
                hit = True
                i = middle
                while i >= 0:
                    if nums[i] == target:
                        i -= 1
                    else:
                        break
                i += 1
                result.append(i)
                while i <= len(nums) - 1 and nums[i] == target:
                    i += 1
                result.append(i - 1)
                break
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        if hit:
            return result
        else:
            return [-1, -1]


assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert Solution().searchRange([1], 1) == [0, 0]
