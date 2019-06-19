# -*- coding:utf-8 -*-


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :param word1: str
        :param word2: str
        :return: int
        """
        # dp[i][j]代表word1[0:i]和word2[0:j]需要修改的次数
        dp = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for i in xrange(len(dp)):
            dp[i][0] = i

        for j in xrange(len(dp[0])):
            dp[0][j] = j

        for i in xrange(1, len(dp)):
            for j in xrange(1, len(dp[0])):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[len(word1)][len(word2)]


assert Solution().minDistance("horse", "ros") == 3
assert Solution().minDistance("intention", "execution") == 5
