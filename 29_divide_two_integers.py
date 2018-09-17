class Solution(object):
    def __init__(self):
        self.MIN_INTEGER = -1 * (1 << 31)
        self.MAX_INTEGER = (1 << 31) - 1

    def divide(self, dividend, divisor):
        """
        :param dividend: int
        :param divisor: int
        :return: int
        """
        result = int(dividend / float(divisor))
        if result > self.MAX_INTEGER:
            result = self.MAX_INTEGER
        # elif result < MIN_INTEGER:
        #     result = MIN_INTEGER
        return result


assert Solution().divide(-2147483648, -1) == 2147483647
assert Solution().divide(10, 3) == 3
