class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = len(flowerbed)
        if count == 1 and flowerbed[0] == 0:
            return n <= 1
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[count-1] == 0 and flowerbed[count-2] == 0:
            flowerbed[count-1] = 1
            n -= 1

        i = 1
        while i + 1 < count:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            i += 1

        return n <= 0

assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
assert Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) == False
assert Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2) == True
assert Solution().canPlaceFlowers([0, 0, 1, 0, 0], 2) == True