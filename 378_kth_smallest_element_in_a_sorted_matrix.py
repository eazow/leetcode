import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        elements = list(heapq.merge(*matrix))
        return elements[k-1]


assert Solution().kthSmallest([
       [1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ], 8) == 13
