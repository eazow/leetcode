class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = s.split(' ')
        reverseStrs= []
        for tempStr in strs:
            reverseStrs.append(tempStr[::-1])

        return ' '.join(reverseStrs)

assert Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"