import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        width = int(math.sqrt(area))
        while area%width != 0:
            width -= 1
        return [area/width, width]

Solution().constructRectangle(4) == [2,2]
Solution().constructRectangle(10) == [5,2]