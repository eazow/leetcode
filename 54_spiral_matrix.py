class Solution(object):
    def __init__(self):
        self.row_col_set = set()
        self.nums = []

    def add(self, row_col, num):
        if row_col not in self.row_col_set:
            self.row_col_set.add(row_col)
            self.nums.append(num)

    def spiralOrder(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        cols_count = len(matrix[0])
        rows_count = len(matrix)

        row = 0
        col = 0
        height = 0
        while height * 2 < rows_count:
            # right
            for col in xrange(col, cols_count - height):
                self.add((row, col), matrix[row][col])

            row += 1
            if row >= rows_count:
                break

            # down
            for row in xrange(row, rows_count - height):
                self.add((row, col), matrix[row][col])

            col -= 1
            if col < 0:
                break

            # left
            for col in xrange(col, height - 1, -1):
                self.add((row, col), matrix[row][col])

            row -= 1
            height += 1

            # up
            for row in xrange(row, height - 1, -1):
                self.add((row, col), matrix[row][col])

            col += 1

        return self.nums


assert Solution().spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

assert Solution().spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

assert Solution().spiralOrder([
    [2, 5, 8],
    [4, 0, -1]
]) == [2, 5, 8, -1, 0, 4]

assert Solution().spiralOrder([[2, 3]]) == [2, 3]

assert Solution().spiralOrder([[7], [9], [6]]) == [7, 9, 6]
