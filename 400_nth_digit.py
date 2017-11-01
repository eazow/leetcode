class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = ""
        i = 1
        while i <= n:
            digits += str(i)
            if len(digits) >= n:
                return int(digits[n-1])
            i += 1

assert Solution().findNthDigit(3) == 3
assert Solution().findNthDigit(11) == 0