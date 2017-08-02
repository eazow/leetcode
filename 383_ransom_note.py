class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)

        i = 0
        j = 0
        while i < len(ransomNote) and j < len(magazine):
            if ransomNote[i] == magazine[j]:
                j += 1
                i += 1
            else:
                j += 1
   
        if i == len(ransomNote):
            return True
        return False

assert Solution().canConstruct("a", "b") == False
assert Solution().canConstruct("aa", "ab") == False
assert Solution().canConstruct("aa", "aab") == True
assert Solution().canConstruct("djfjfhjf", "aaigcbiafifghhdihcfdjjej") == True