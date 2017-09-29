class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

assert Solution().countSegments("Hello, my name is John") == 5
assert Solution().countSegments("") == 0