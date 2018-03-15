class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        rtype: str
        """
        def replace(word, roots_set):
            for i in range(len(word)):
                if word[0:i] in roots_set:
                    return word[0:i]
            return word

        roots_set = set(dict)
        words = []
        for word in sentence.split(" "):
            words.append(replace(word, roots_set))
        return " ".join(words)

assert Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattle by the battery") == "the cat was rat by the bat"