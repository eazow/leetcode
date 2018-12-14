class Solution(object):
    def multiply(self, num1, num2):
        """
        :param num1: str
        :param num2: str
        :return: str
        """
        # return str(int(num1) * int(num2))

        result = 0
        for i in xrange(len(num1)-1, -1, -1):
            for j in xrange(len(num2)-1, -1, -1):
                base = 1
                for k in xrange((len(num1) - 1 - i) + (len(num2) - 1 - j)):
                    base *= 10
                result += int(num1[i]) * int(num2[j]) * base

        return str(result)


# assert Solution().multiply("2", "3") == "6"
print Solution().multiply("123", "456")
