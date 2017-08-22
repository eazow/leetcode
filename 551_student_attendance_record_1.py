class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count = 0
        l_count = 0
        for c in s:
            if c == "A":
                a_count += 1
                l_count = 0
                if a_count > 1:
                    return False
            elif c == "L":
                l_count += 1
                if l_count > 2:
                    return False
            else:
                l_count = 0

        return True

assert Solution().checkRecord("PPALLP") == True
assert Solution().checkRecord("PPALLL") == False
assert Solution().checkRecord("ALPP") == True