# -*- coding:utf-8 -*-


class Solution(object):
    def solveNQueens(self, n):
        """
        :param n: int
        :return: List[List[str]]
        """
        self.n = n
        # locations用于记录Queens的位置信息，如果locations[i]==j，表示坐标(i, j)有一个Queen
        locations = [-1] * n
        self.results = []
        self.dfs(locations, 0)
        return self.results

    def dfs(self, locations, row):
        """
        递归处理
        :param locations:
        :param row:
        :return:
        """
        # row == self.n，表示全部Queen已找到位置
        if row == self.n:
            self.results.append(self.parse_locations_to_result(locations))
            return
        for i in range(self.n):
            if self.check(locations, row, i):
                locations[row] = i
                self.dfs(locations, row+1)
                # 将第row行的Queen置为-1，表示又可以放置Queen
                locations[row] = -1

    def parse_locations_to_result(self, locations):
        """
        将存储位置信息的数组转换为结果数组
        如将[1,4,0,2]转换为[".Q..", "...Q", "Q...", "..Q."]
        :param locations:
        :return:
        """
        result = []
        for location in locations:
            result.append("." * location + "Q" + "." * (self.n - 1 - location))
        return result

    def check(self, locations, row, col):
        """
        检查(row, col)位置是否可以放置Queen
        :param locations:
        :param row:
        :param col:
        :return:
        """
        for the_index in range(self.n):
            location = locations[the_index]

            if location != -1:
                # 检查水平、垂直方向是否有Queen
                if location == col or the_index == row:
                    return False

                # 这道题效率的关键点, 检查对角线是否有Queen
                if (row - col == the_index - location) or (row + col == the_index + location):
                    return False

        return True


assert Solution().solveNQueens(4) == [
    [
        ".Q..",
        "...Q",
        "Q...",
        "..Q."
    ],
    [
        "..Q.",
        "Q...",
        "...Q",
        ".Q.."
    ]
]