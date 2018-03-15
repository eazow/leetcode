class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        rtype: int
        """
        a_b_sum_map = {}
        for i in range(len(A)):
            for j in range(len(B)):
                the_sum = A[i] + B[j]
                if the_sum not in a_b_sum_map:
                    a_b_sum_map[the_sum] = 0
                a_b_sum_map[the_sum] += 1

        count = 0
        for i in range(len(C)):
            for j in range(len(D)):
                the_sum = -1 * (C[i] + D[j])
                if the_sum in a_b_sum_map:
                    count += a_b_sum_map[the_sum]

        return count

assert Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2