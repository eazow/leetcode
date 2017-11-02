class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 1
        count = 9
        start_num = 1

        while n > bits * count:
            n -= bits * count
            bits += 1
            count *= 10
            start_num *= 10

        if n % bits == 0:
            num = n / bits - 1 + start_num
            return int(str(num)[-1])
        else:
            num = n / bits + start_num
            return int(str(num)[n % bits - 1])


assert Solution().findNthDigit(2) == 2
assert Solution().findNthDigit(10) == 1
assert Solution().findNthDigit(11) == 0