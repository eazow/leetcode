class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies)/2, len(set(candies)))

assert Solution().distributeCandies([1,1,2,2,3,3]) == 3
assert Solution().distributeCandies([1,1,2,3]) == 2
assert Solution().distributeCandies([1,1,1,1]) == 1