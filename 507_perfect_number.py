class Solution(object):
    """
    @Time Exceeded
    def checkPerfectNumber(self, num):
        if num <= 0:
            return False
        i = 1
        sum = 0
        while i <= num/2:
            if num % i == 0:
                sum += i
            i += 1
        return sum == num
    """

    def checkPerfectNumber(self, num):
        if num == 1:
            return False
        sum = 1
        i = 2
        while i * i < num:
            if num % i == 0:
                sum += i + num/i
            i += 1
        if i * i == num:
            sum += i
        return sum == num

assert Solution().checkPerfectNumber(1) == False
assert Solution().checkPerfectNumber(28) == True
assert Solution().checkPerfectNumber(13466917) == False