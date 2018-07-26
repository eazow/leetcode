class Solution(object):
    def longestPalindrome(self, s):
        """
        :param s: str
        :return: str
          a b c b
        a 1 0 0 0
        b   1 0 1
        c     1 0
        b       1
        """
        dp = [[False for col in range(len(s))] for row in range(len(s))]
        length = 0
        max_length = 0
        start = 0
        end = 0
        while length < len(s):
            i = 0
            while i + length < len(s):
                j = i + length
                if length == 1 or length == 0:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j] and max_length < length + 1:
                    max_length = length + 1
                    start = i
                    end = j
                i += 1
            length += 1

        return s[start:end+1]


assert Solution().longestPalindrome("abcbaabc") == "cbaabc"
