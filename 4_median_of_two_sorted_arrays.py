class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        """
        nums = nums1 + nums2
        nums = sorted(nums)
        nums_len = len(nums)
        if nums_len % 2 == 0:
            return (nums[nums_len/2-1] + nums[nums_len/2]) / 2.0
        else:
            return nums[nums_len/2]


assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
