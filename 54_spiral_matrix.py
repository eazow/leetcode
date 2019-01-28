class Solution(object):
    def spiralOrder(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        cols_count = len(matrix[0])
        rows_count = len(matrix)

        results = []
        row = 0
        col = 0
        height = 0
        row_col_set = set()
        while height <= rows_count:
            while col < cols_count - height:
                if (row, col) not in row_col_set:
                    results.append(matrix[row][col])
                    row_col_set.add((row, col))
                col += 1
            col -= 1
            row += 1
            while row < rows_count - height:
                if (row, col) not in row_col_set:
                    results.append(matrix[row][col])
                    row_col_set.add((row, col))
                row += 1

            row -= 1
            col -= 1

            while col >= height:
                if (row, col) not in row_col_set:
                    results.append(matrix[row][col])
                    row_col_set.add((row, col))
                col -= 1

            col += 1
            row -= 1
            height += 1
            while row >= height:
                if (row, col) not in row_col_set:
                    results.append(matrix[row][col])
                    row_col_set.add((row, col))
                row -= 1

            row += 1
            col += 1

        return results


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
