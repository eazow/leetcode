NUM = 6

def guess(num):
    if num == NUM:
        return 0
    elif NUM < num:
        return -1
    return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            middle = (left+right)/2
            guessResult = guess(middle)
            if guessResult == 0:
                return middle
            elif guessResult == -1:
                right = middle-1
            else:
                left = middle+1
        return left

assert Solution().guessNumber(10) == 6
