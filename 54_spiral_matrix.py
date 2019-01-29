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
        while height * 2 < rows_count:
            # right
            add_flag = False
            for col in range(col, cols_count - height):
                results.append(matrix[row][col])
                add_flag = True

            if not add_flag:
                break

            row += 1
            # down
            add_flag = False
            for row in range(row, rows_count - height):
                results.append(matrix[row][col])
                add_flag = True

            if not add_flag:
                break
            col -= 1

            # left
            add_flag = False
            for col in range(col, height - 1, -1):
                results.append(matrix[row][col])
                add_flag = True

            if not add_flag:
                break

            row -= 1
            height += 1

            # up
            for row in range(row, height - 1, -1):
                results.append(matrix[row][col])

            col += 1

        print results
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

Solution().spiralOrder([
    [2, 5, 8],
    [4, 0, -1]
])
