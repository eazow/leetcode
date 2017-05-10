class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        numsRows = len(nums)
        numsCols = len(nums[0])
        if numsRows*numsCols != r*c:
            return nums
        result = [[0 for col in range(c)] for row in xrange(r)]
        i = 0
        while i < r*c:
            result[i/c][i%c] = nums[i/numsCols][i%numsCols]
            i += 1

        return result

assert Solution().matrixReshape([[1,2],[3,4]], 1, 4) == [[1,2,3,4]]
assert Solution().matrixReshape([[1,2],[3,4]], 2, 4) == [[1,2],[3,4]]
assert Solution().matrixReshape([[1,2,3,4]], 2, 2) == [[1,2],[3,4]]