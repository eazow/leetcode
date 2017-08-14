class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        for c in s:
            if counter.has_key(c):
                counter[c] += 1
            else:
                counter[c] = 1

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1

assert Solution().firstUniqChar("leetcode") == 0
assert Solution().firstUniqChar("leveleetcode") == 2