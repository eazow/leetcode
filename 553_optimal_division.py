class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        if len(nums) <= 2:
            return '/'.join(nums)
        
        return "%s/(%s)" % (str(nums[0]), '/'.join(nums[1:]))

assert Solution().optimalDivision([1000,100,10,2]) == '1000/(100/10/2)'
assert Solution().optimalDivision([2]) == '2'