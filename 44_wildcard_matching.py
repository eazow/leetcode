class Solution(object):
    def isMatch(self, s, p):
        dp = [[False for col in xrange(len(p))] for row in xrange(len(s))]

        if len(p) == 0 and len(s) == 0:
            return True
        elif len(p) == 0:
            return False
        elif len(s) == 0:
            if p.count("*") == len(p):
                return True
            return False

        dp[0][0] = False
        if s[0] == p[0] or p[0] == "?" or p[0] == "*":
            dp[0][0] = True

        for i in xrange(1, len(s)):
            if p[0] == "*":
                dp[i][0] = True
            else:
                break

        question_mark_or_alpha = False
        if p[0] == "?" or p[0] == s[0]:
            question_mark_or_alpha = True
        for j in xrange(1, len(p)):
            if p[j] == "*":
                dp[0][j] = dp[0][j-1]
            elif (s[0] == p[j] or p[j] == "?") and not question_mark_or_alpha:
                dp[0][j] = dp[0][j-1]
                question_mark_or_alpha = True
            else:
                dp[0][j] = False

        for i in xrange(1, len(s)):
            for j in xrange(1, len(p)):
                if s[i] == p[j] or p[j] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False

        return dp[len(s)-1][len(p)-1]


assert Solution().isMatch("", "*") is True
assert Solution().isMatch("b", "?*?") is False
assert Solution().isMatch("c", "*?*") is True
assert Solution().isMatch("ab", "?*?*") is True
assert Solution().isMatch("abbbba", "a**a*?") is False
assert Solution().isMatch("aab", "c*a*b") is False
assert Solution().isMatch("aa", "a") is False
assert Solution().isMatch("a", "aa") is False
assert Solution().isMatch("aa", "*") is True
assert Solution().isMatch("cb", "?a") is False
assert Solution().isMatch("adceb", "*a*b") is True
assert Solution().isMatch("acdcb", "a*c?b") is False
assert Solution().isMatch("", "") is True
assert Solution().isMatch("ho", "ho**") is True
assert Solution().isMatch("bbbbbbbbaaabbaabbabaaaaaabbbababbbaaabbaabbbababbaaaa", "**a*bbaabb**bbab*a**") is True
# RuntimeError: maximum recursion depth exceeded in cmp
assert Solution().isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*") is False
