import re

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            if re.match("(?i)^(([qwertyuiop]+)|([asdfghjkl]*)|([zxcvbnm]+))$", word):
                result.append(word)
        return result

assert Solution().findWords(["Hello","Alaska","Dad","Peace"]) == ["Alaska","Dad"]