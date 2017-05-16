class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 2
        result = 0
        seriesNum = 0
        while i < len(A):
            if A[i-1]-A[i-2] == A[i]-A[i-1]:
                seriesNum += 1
                result += seriesNum
            else:
                seriesNum = 0
            i += 1

        return result

assert Solution().numberOfArithmeticSlices([1,2,3,4]) == 3
assert Solution().numberOfArithmeticSlices([1,2,3,4,5]) == 6
assert Solution().numberOfArithmeticSlices([1,2,3,8,9,10]) == 2