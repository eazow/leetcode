class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for start in range(len(s)):
            for end in range(start+1, len(s) + 1):
                temp_str = s[start: end]
                if temp_str == temp_str[::-1]:
                    count += 1
        return count

assert Solution().countSubstrings("abc") == 3
assert Solution().countSubstrings("aaa") == 6