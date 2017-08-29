class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        num = ""
        carry = 0
        while i >= 0 or j >= 0:
            result = carry
            if i >= 0:
                result += int(num1[i])
            if j >= 0:
                result += int(num2[j])
            if result >= 10:
                carry = 1
            else:
                carry = 0
            num = str(result % 10) + num
            i -= 1
            j -= 1
        if carry == 1:
            num = "1" + num
        return num

assert Solution().addStrings("111", "234965") == "235076"
assert Solution().addStrings("999", "1") == "1000"