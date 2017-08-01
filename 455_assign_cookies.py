class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        i = 0
        content_count = 0
        for greed in g:
            while i < len(s):
                if s[i] >= greed:
                    content_count += 1
                    i += 1
                    break
                i += 1
            else:
                break

        return content_count

assert Solution().findContentChildren([1, 2 ,3], [1, 1]) == 1
assert Solution().findContentChildren([1, 2], [1, 2, 3]) == 2
assert Solution().findContentChildren([1, 2, 3], []) == 0
assert Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]) == 2
assert Solution().findContentChildren([1, 2, 3], [3]) == 1