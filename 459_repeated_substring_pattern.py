class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)
        substring_len = s_len/2
        while substring_len >= 1:
            if s_len % substring_len == 0:
                count = s_len / substring_len
                substring = s[0:substring_len]
                if substring * count == s:
                    return True
            substring_len -= 1
        return False

assert Solution().repeatedSubstringPattern("abab") == True
assert Solution().repeatedSubstringPattern("aba") == False
assert Solution().repeatedSubstringPattern("abcabcabcabc") == True