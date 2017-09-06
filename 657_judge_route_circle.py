class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        counter = {}
        for c in moves:
            counter[c] = counter.get(c, 0) + 1

        return counter.get("L") == counter.get("R") and counter.get("U") == counter.get("D")

assert Solution().judgeCircle("UD") == True
assert Solution().judgeCircle("LL") == False