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
        i = 0
        sorted_p = "".join(sorted(p))
        anagrams = []
        while i <= len(s)-len(p):
            temp_s = s[i: i + len(p)]
            sorted_temp_s = "".join(sorted(temp_s))
            if sorted_temp_s == sorted_p:
                anagrams.append(i)
            i += 1
        return anagrams

assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]