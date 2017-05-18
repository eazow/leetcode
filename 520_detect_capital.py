class Solution(object):
    def detectCapitalUse(self, word):
        capitalsCount = 0
        for i in range(len(word)):
            if word[i].isupper():
                capitalsCount += 1

        if capitalsCount==0 or capitalsCount==len(word) or (capitalsCount==1 and word[0].isupper()):
            return True
        return False

assert Solution().detectCapitalUse("USA") == True
assert Solution().detectCapitalUse("FlaG") == False