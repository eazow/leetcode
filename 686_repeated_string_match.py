class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(B) % len(A) == 0:
            count = len(B) / len(A)
        else:
            count = len(B) / len(A) + 1
        if count == 0:
            count = 1
        repeated = A * count
        if repeated.find(B) >= 0:
            return count
        else:
            count += 1
            repeated += A
            if repeated.find(B) >= 0:
                return count
        return -1


assert Solution().repeatedStringMatch("abcd", "cdabcdab") == 3
assert Solution().repeatedStringMatch("a", "aa") == 2
assert Solution().repeatedStringMatch("abcde", "cdabcdab") == -1
assert Solution().repeatedStringMatch("abababaaba", "aabaaba") == 2