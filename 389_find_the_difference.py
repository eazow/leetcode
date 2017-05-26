class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i = 0
        difference = 0
        for i in xrange(len(s)):
            difference ^= ord(s[i]) ^ ord(t[i])

        return chr(difference ^ ord(t[-1]))

assert Solution().findTheDifference("abcd", "abcde")  == "e"