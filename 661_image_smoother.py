from copy import deepcopy

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        result = deepcopy(M)
        for i in range(len(M)):
            for j in range(len(M[i])):
                x = i - 1
                count = 0
                the_sum = 0
                while x <= i + 1:
                    if x >= 0 and x < len(M):
                        y = j - 1
                        while y <= j + 1:
                            if y >= 0 and y < len(M[i]):
                                count += 1
                                the_sum += M[x][y]
                            y += 1
                    x += 1
                result[i][j] = int(the_sum / count) if count > 0 else 0

        return result

assert Solution().imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
assert Solution().imageSmoother([[10,8,1],[5,1,5],[6,5,2]]) == [[6, 5, 3],[5, 4, 3],[4, 4, 3]]