# -*- coding:utf-8 -*-

class Solution(object):
    def trap(self, height):
        """
        1. 找到容器最高点位置max_height_index, 最高点高度max_height。找到最高点后，左边和右边的bar都能跟其形成容器蓄水
        2. 从左往右处理至max_height_index, left_max记录遍历时左边区间的最高高度, 如果height[i] > left_max, 则该格无法蓄水，
           将left_max更新为height[i]; 如果height[i] < left_max，则该格可以蓄水left_max - height[i]
        3. 从右往左处理至max_height_index，right_max记录遍历时右边区间的最高高度，如果height[i] > right_max, 则该格无法蓄水，
           将right_max更新为height[i]; 如果height[i] < right_max，则该格可以蓄水left_max - height[i]
        4. 将每格可以蓄的水累加即可
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

