from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_s = len(s)
        len_p = len(p)
        if len_s < len(p):
            return []
        temp_s = s[0: len_p]
        counter_s = Counter(temp_s)
        counter_p = Counter(p)

        anagrams = []
        if counter_s == counter_p:
            anagrams.append(0)

        i = 1
        while i + len_p <= len_s:
            counter_s[s[i+len_p-1]] += 1
            counter_s[s[i-1]] -= 1
            if counter_s[s[i-1]] == 0:
                del counter_s[s[i-1]]
            if counter_s == counter_p:
                anagrams.append(i)
            i += 1

        return anagrams

assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]