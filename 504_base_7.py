class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        symbol = ""
        if num < 0:
            num = 0 - num
            symbol = "-"

        result = ""
        while num > 0:
            result += str(num % 7)
            num = num / 7

        return symbol + result[::-1]

assert Solution().convertToBase7(100) == "202"
assert Solution().convertToBase7(-7) == "-10"