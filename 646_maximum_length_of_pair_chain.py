class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        cur = float("-inf")
        count = 0
        pairs = sorted(pairs, cmp=lambda x, y: cmp(x[1], y[1]))
        for pair in pairs:
            if cur < pair[0]:
                count += 1
                cur = pair[1]
        return count


assert Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2