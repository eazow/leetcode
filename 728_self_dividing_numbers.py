class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []
        for num in range(left, right+1):
            if self.isDividingNumber(num):
                nums.append(num)
        return nums

    def isDividingNumber(self, num):
        origin_num = num
        while num:
            digit = num % 10
            if digit == 0 or origin_num % digit != 0:
                return False
            num = num / 10
        return True

assert Solution().selfDividingNumbers(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]