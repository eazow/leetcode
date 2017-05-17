class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicates = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index] < 0:
                duplicates.append(index+1)
            else:
                nums[index] = -nums[index]

        return duplicates

assert Solution().findDuplicates([4,3,2,7,8,2,3,1]) == [2,3]
assert Solution().findDuplicates([10,2,5,10,9,1,1,4,3,7]) == [10,1]