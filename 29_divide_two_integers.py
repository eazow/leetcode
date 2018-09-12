MIN_INTEGER = -1 * (1 << 31)
MAX_INTEGER = (1 << 31) - 1


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :param dividend: int
        :param divisor: int
        :return: int
        """
        result = int(dividend / float(divisor))
        if result > MAX_INTEGER:
            result = MAX_INTEGER
        # elif result < MIN_INTEGER:
        #     result = MIN_INTEGER
        return result


assert Solution().divide(-2147483648, -1) == 2147483647
assert Solution().divide(10, 3) == 3
