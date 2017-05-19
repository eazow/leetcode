class Solution(object):
    def detectCapitalUse(self, word):
        length = len(word)

        firstIsCapital = word[0].isupper()
        i = 1
        hasLower = False
        hasCapital = False
        while i < length:
            if word[i].islower():
                hasLower = True
            else:
                hasCapital = True
            if hasLower and hasCapital:
                return False
            i += 1

        if not firstIsCapital and hasCapital:
            return False

        return True

"""
    def detectCapitalUse(self, word):
        capitalsCount = 0
        for i in range(len(word)):
            if word[i].isupper():
                capitalsCount += 1

        if capitalsCount==0 or capitalsCount==len(word) or (capitalsCount==1 and word[0].isupper()):
            return True
        return False
"""

assert Solution().detectCapitalUse("USA") == True
assert Solution().detectCapitalUse("FlaG") == False
assert Solution().detectCapitalUse("ABc") == False
assert Solution().detectCapitalUse("Leetcode") == True
assert Solution().detectCapitalUse("aBC") == False