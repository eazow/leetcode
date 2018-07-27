class Solution(object):
    def isMatch(self, s, p):
        """
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


print Solution().isMatch("aa", "a")
print Solution().isMatch("aa", "a*")
print Solution().isMatch("ab", ".*")
print Solution().isMatch("aab", "c*a*b")
print Solution().isMatch("mississippi", "mis*is*p*.")