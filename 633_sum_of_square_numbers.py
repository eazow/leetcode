import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            square_sum = left * left + right * right
            if square_sum < c:
                left += 1
            elif square_sum > c:
                right -= 1
            else:
                return True
        return False

assert Solution().judgeSquareSum(5) == True
assert Solution().judgeSquareSum(3) == False