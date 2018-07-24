class Solution(object):
    def minSteps(self, n):
        """
        :param n: int
        :return: int
        """
        if n == 1:
            return 0

        copy_length = 1
        steps = 1
        length = 1
        while n - length > copy_length:
            if (n - length - copy_length) % (length + copy_length) == 0:
                length += copy_length
                copy_length = length
                steps += 2
            else:
                steps += 1
                length += copy_length
        return steps + 1


assert Solution().minSteps(1) == 0
assert Solution().minSteps(3) == 3
assert Solution().minSteps(5) == 5
assert Solution().minSteps(100) == 14
