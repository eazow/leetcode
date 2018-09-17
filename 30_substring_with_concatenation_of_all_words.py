# -*- coding: utf-8 -*-

class Solution(object):
    def findSubstring(self, s, words):
        """
        :param s: str
        :param words: List[str]
        :return: List[int]
        """
        words_count = len(words)
        if words_count == 0 or len(s) == 0:
            return []

        result = []
        word_length = len(words[0])
        words_length = words_count * word_length
        s_length = len(s)

        for i in range(s_length - words_length + 1):
            temp_s = s[i:i+words_length]
            temp_words = words[:]
            # 找出temp_s是否和temp_words匹配
            j = 0
            temp_s_map = {}
            while j < len(temp_s):
                if temp_s[j:j+word_length] in temp_s_map:
                    temp_s_map[temp_s[j:j+word_length]] += 1
                else:
                    temp_s_map[temp_s[j:j + word_length]] = 1
                j += word_length

            match = True
            for word in temp_words:
                if word in temp_s_map:
                    temp_s_map[word] -= 1
                    if temp_s_map[word] == 0:
                        del temp_s_map[word]
                else:
                    match = False
                    break

            if match:
                result.append(i)

        return result


assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
assert Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]) == []
assert Solution().findSubstring("ababaab", ["ab", "ba", "ba"]) == [1]
