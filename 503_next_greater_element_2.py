class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums)
        stack = []
        for i in range(len(nums))*2:
            while stack and (nums[stack[-1]] < nums[i]):
                result[stack.pop()] = nums[i]
            stack.append(i)

        return result

assert Solution().nextGreaterElements([1,2,1]) == [2,-1,2]