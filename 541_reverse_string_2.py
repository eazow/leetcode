class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        while s:
            temp = s[0:k]
            result += temp[::-1] + s[k:2*k]
            s = s[2*k:]
        return result

assert Solution().reverseStr("abcdefg", 2) == "bacdfeg"