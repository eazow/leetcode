# -*- coding:utf-8 -*-

class Solution(object):
    def trap(self, height):
        """
        :param height: List[int]
        :return: int
        """
        result = 0
        max_height = 0
        max_height_index = 0
        for i in xrange(len(height)):
            if height[i] > max_height:
                max_height = height[i]
                max_height_index = i

        left_max = 0
        for i in xrange(0, max_height_index):
            if height[i] > left_max:
                left_max = height[i]
            else:
                result += left_max - height[i]

        right_max = 0
        for i in xrange(len(height)-1, max_height_index, -1):
            if height[i] > right_max:
                right_max = height[i]
            else:
                result += right_max - height[i]

        return result


assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

