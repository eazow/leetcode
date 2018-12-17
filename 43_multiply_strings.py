class Solution(object):
    def multiply(self, num1, num2):
        """
        :param num1: str
        :param num2: str
        :return: str
        """
        # return str(int(num1) * int(num2))

        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                result[i+j] += int(num1[i]) * int(num2[j])

                if result[i+j] >= 10:
                    result[i+j+1] += result[i+j] / 10
                    result[i+j] = result[i+j] % 10

        result = result[::-1]
        i = 0
        while result[i] == 0:
            i += 1

        return "".join(map(str, result[i:]))


assert Solution().multiply("2", "3") == "6"
assert Solution().multiply("0", "0") == "0"
assert Solution().multiply("123", "456") == "56088"
