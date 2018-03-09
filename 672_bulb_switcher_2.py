class Solution(object):
    def flipLights(self, n, m):
        """
        1,2=3  1,3=2
        8种状态 all_on 1 2 3 4 (1,4) (2,4) (3,4)
        :type n: int
        :type m: int
        :rtype: int
        """
        result = 0
        
        if m == 0:
            result = 1
        elif n == 1:
            result = 2
        elif m == 1:
            if n == 2:
                result = 3
            else:
                result = 4
        elif m == 2:
            if n == 1:
                result = 2
            elif n == 2:
                result = 4
            else:
                result = 7
        elif m == 3:
            if n == 2:
                result = 4
            else:
                result = 8
        else:
            if n == 2:
                result = 4
            else:
                result = 8

        return result

assert Solution().flipLights(1, 1) == 2
assert Solution().flipLights(2, 1) == 3
assert Solution().flipLights(3, 1) == 4
assert Solution().flipLights(2, 1000) == 4