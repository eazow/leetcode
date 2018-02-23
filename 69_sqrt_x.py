class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def search(left, right, target):
            middle = (left + right) / 2

            if middle * middle == target:
                return middle
            elif left +1 == right and left * left < target and right * right > target:
                return left
            elif left >= right:
                return middle
            elif target < middle * middle:
                right = middle
            else:
                left = middle
            return search(left, right, target)

        return search(1, x, x)

assert Solution().mySqrt(1) == 1
assert Solution().mySqrt(8) == 2
assert Solution().mySqrt(10) == 3