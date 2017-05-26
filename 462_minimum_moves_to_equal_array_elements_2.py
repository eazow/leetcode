class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves = 0
        medium = len(nums)/2
        for i in xrange(len(nums)):
            moves += abs(nums[i]-nums[medium])

        return moves

assert Solution().minMoves2([1,2,3]) == 2