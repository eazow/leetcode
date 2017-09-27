class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1
        error_nums = []
        nums_set = set()
        for num in nums:
            if num in nums_set:
                error_nums.append(num)
            else:
                nums_set.add(num)

        i = 1
        while i <= len(nums):
            if i not in nums_set:
                error_nums.append(i)
                break
            i += 1

        return error_nums

assert Solution().findErrorNums([1, 2, 2, 4]) == [2, 3]