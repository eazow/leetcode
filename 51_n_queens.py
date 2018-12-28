# -*- coding:utf-8 -*-
import copy

class Solution():
    def solveNQueens(self, n):
        """
        :param n: int
        :return: List[List[str]]
        """
        self.n = n
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
            locations_copy = locations[:]
            if self.check(locations_copy, row, i):
                locations_copy[row] = i
                self.dfs(locations_copy, row+1)

    def parse_locations_to_result(self, locations):
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
        queen_locations_set = set()
        n = self.n

        for the_index in range(self.n):
            location = locations[the_index]

            if location != -1:
                for i in range(n):
                    queen_locations_set.add((i, location))
                for j in range(n):
                    queen_locations_set.add((the_index, j))

                i = the_index
                j = location
                while i < n and j < n:
                    queen_locations_set.add((i, j))
                    i += 1
                    j += 1
                i = the_index
                j = location
                while i >= 0 and j < n:
                    queen_locations_set.add((i, j))
                    i -= 1
                    j += 1
                i = the_index
                j = location
                while i < n and j >= 0:
                    queen_locations_set.add((i, j))
                    i += 1
                    j -= 1
                i = the_index
                j = location
                while i >= 0 and j >= 0:
                    queen_locations_set.add((i, j))
                    i -= 1
                    j -= 1

        if (row, col) in queen_locations_set:
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