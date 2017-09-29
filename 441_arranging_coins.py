class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        lines = 0
        while n >= i:
            n -= i
            lines += 1
            i += 1
        return lines

assert Solution().arrangeCoins(5) == 2
assert Solution().arrangeCoins(8) == 3