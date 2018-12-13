class Solution(object):
    def multiply(self, num1, num2):
        """
        :param num1: str
        :param num2: str
        :return: str
        """
        return str(int(num1) * int(num2))


assert Solution().multiply("2", "3") == "6"