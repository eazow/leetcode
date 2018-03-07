class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words_set = set()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            for i in range(len(word)):
                c = word[i]
                for j in range(26):
                    alpha = chr(ord('a') + j)
                    if alpha != c:
                        new_word = word[0:i] + alpha + word[i+1:]
                        self.words_set.add(new_word)


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exatly one character
        :type word: str
        :rtype: bool
        """
        return word in self.words_set

dictionary = MagicDictionary()
dictionary.buildDict(["hello", "leetcode"])
assert dictionary.search("hello") == False
assert dictionary.search("hhllo") == True
assert dictionary.search("hell") == False
assert dictionary.search("leetcoded") == False