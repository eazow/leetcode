class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        result = 0
        while i <= num:
            result |= (i & num) ^ i
            i <<= 1
            
        return result

assert Solution().findComplement(5) == 2
assert Solution().findComplement(1) == 0