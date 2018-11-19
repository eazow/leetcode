class Solution(object):
    def __init__(self):
        self.result_map = {}

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
                dp[i][0] = False

        question_marks = 0
        if p[0] == "?":
            question_marks = 1
        for j in xrange(1, len(p)):
            if p[j] == "*":
                dp[0][j] = dp[0][j-1]
            elif p[j-1] == "*" and (s[0] == p[j] or p[j] == "?") and question_marks == 0:
                dp[0][j] = dp[0][j-1]
                question_marks += 1
            # else:
            #     dp[0][j] = False

        for row in dp:
            print row

        for i in xrange(1, len(s)):
            for j in xrange(1, len(p)):
                if s[i] == p[j] or p[j] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False

        return dp[len(s)-1][len(p)-1]


    """
    def isMatch(self, s, p):
    """
    """
        :param s: str
        :param p: str
        :return: bool
    """
    """
    token = s + "#" + p
    if token in self.result_map:
        return self.result_map.get(token)

    if len(s) == 0:
        if len(p) == 0:
            result = True
        elif p[0] == "*":
            result = self.isMatch(s, p[1:])
        else:
            result = False
    elif len(p) == 0:
        result = False
    elif s[0] == p[0]:
        result = self.isMatch(s[1:], p[1:])
    elif p[0] == "?":
        result = self.isMatch(s[1:], p[1:])
    elif p[0] == "*":
        result = self.isMatch(s[1:], p) or self.isMatch(s[1:], p[1:]) or self.isMatch(s, p[1:])
    else:
        result = False

    self.result_map[token] = result
    return result
"""

# assert Solution().isMatch("b", "?*?") == False
# assert Solution().isMatch("c", "*?*") == True
# assert Solution().isMatch("ab", "?*?*") == True
assert Solution().isMatch("abbbba", "a**a*?") == False
# print Solution().isMatch("aab", "c*a*b")
# print Solution().isMatch("aa", "a")
# print Solution().isMatch("a", "aa")
# # print Solution().isMatch("aa", "*")
# # print Solution().isMatch("cb", "?a")
# print Solution().isMatch("adceb", "*a*b")
# print Solution().isMatch("acdcb", "a*c?b")
# print Solution().isMatch("", "")
# print Solution().isMatch("ho", "ho**")
# print Solution().isMatch("bbbbbbbbaaabbaabbabaaaaaabbbababbbaaabbaabbbababbaaaa", "**a*bbaabb**bbab*a**")
# # RuntimeError: maximum recursion depth exceeded in cmp
# print Solution().isMatch("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*")
