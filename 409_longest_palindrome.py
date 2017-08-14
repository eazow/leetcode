class Solution(object):
    def longestPalindrome(self, s):
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

        palindrome_length = 0
        single = False
        for key in counter:
            if counter[key] % 2 == 0:
                palindrome_length += counter[key]
            elif counter[key] > 1:
                palindrome_length += counter[key] - 1
                single = True
            elif counter[key] == 1:
                single = True

        if single:
            palindrome_length += 1

        return palindrome_length

assert Solution().longestPalindrome("abccccdd") == 7