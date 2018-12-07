class Solution(object):
    def myPow(self, x, n):
        """
        :param x: float
        :param n: int
        :return: float
        """
        negative = False

        if n == 0:
            return 1
        elif n < 0:
            negative = True
            n = -1 * n

        i = 1
        result = x
        while i <= n:
            if i + i <= n:
                result *= result
                i += i
            else:
                result *= x
                i += 1

        if negative:
            result = 1 / float(result)

        return result


print Solution().myPow(2, 10)
print Solution().myPow(2.1, 3)
print Solution().myPow(2, -2)
print Solution().myPow(0.00001, 2147483647)
