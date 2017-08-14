class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int 
        :type n: int
        :type ops: List[List[int]]
        :rtype int
        """
        rowsCount = m
        colsCount = n
        for op in ops:
            line, col = op
            rowsCount = min(rowsCount, line)
            colsCount = min(colsCount, col)

        return rowsCount * colsCount

assert Solution().maxCount(3, 3, [[2,2],[3,3]]) == 4