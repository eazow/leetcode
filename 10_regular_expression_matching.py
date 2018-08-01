class Solution(object):
    def isMatch2(self, s, p):
        """
        Runtime: 1896ms
        :param s: str
        :param p: str
        :return: bool
        """
        first_match = False
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) > 0 and len(p) > 0:
            first_match = p[0] in [s[0], "."]

        if len(p) >= 2 and p[1] == "*":
            return (first_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatch(self, s, p):
        """
        Runtime: 112ms
        :param s: str
        :param p: str
        :return: bool
        """
        dp = {}
        i = len(s)
        j = len(p) - 1

        dp[(len(s), len(p))] = True
        while i >= 0:
            j = len(p) - 1
            while j >= 0:
                first_match = True if i < len(s) and (s[i] == p[j] or p[j] == ".") else False
                if j + 1 < len(p) and p[j+1] == "*":
                    dp[(i, j)] = first_match and dp.get((i+1, j), False) or dp.get((i, j + 2), False)
                else:
                    dp[(i, j)] = dp.get((i+1, j+1), False) and first_match

                j -= 1
            i -= 1

        return dp[(0, 0)] if (0, 0) in dp else False


assert Solution().isMatch("aa", "a") is False
assert Solution().isMatch("aa", "a*") is True
assert Solution().isMatch("ab", ".*") is True
assert Solution().isMatch("aab", "c*a*b") is True
assert Solution().isMatch("mississippi", "mis*is*p*.") is False
