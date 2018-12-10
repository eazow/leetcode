class Solution(object):
    def myPow(self, x, n):
        """
        :param x: float
        :param n: int
        :return: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            n = -1 * n
            x = 1.0 / x

        result = self.myPow(x * x, n/2) if n % 2 == 0 else x * self.myPow(x, n - 1)
        return result


assert Solution().myPow(2, 10) == 1024
assert round(Solution().myPow(2.1, 3), 3) == 9.261
assert Solution().myPow(2, -2) == 0.25
assert Solution().myPow(0.00001, 2147483647) == 0
