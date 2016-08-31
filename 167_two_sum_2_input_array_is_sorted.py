class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype List[int]
        """
        left = 0
        right = len(numbers)-1;
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1;
            else:
                right -= 1;
        return []

assert Solution().twoSum([2,3,4], 6) == [1,3]
