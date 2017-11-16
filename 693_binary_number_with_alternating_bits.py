class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bits_count = len(bin(n)) - 2
        binary_num = (1 << bits_count) - 1
        return ((n ^ (n >> 1)) & binary_num) == binary_num


assert Solution().hasAlternatingBits(4) == False
assert Solution().hasAlternatingBits(5) == True
assert Solution().hasAlternatingBits(7) == False
assert Solution().hasAlternatingBits(10) == True
assert Solution().hasAlternatingBits(11) == False