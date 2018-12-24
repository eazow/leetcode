# -*- coding:utf-8 -*-


class Solution(object):
    def solveSudoku(self, board):
        """
        :param board: List[List[int]]
        :return: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        row, col = self.get_empty_cell(board)

        if row == -1:
            return True
        for num in "123456789":
            if self.check_board(board, row, col, num):
                board[row][col] = num
                # 关键点
                if self.solve(board):
                    return True
                board[row][col] = "."

        return False

    def get_empty_cell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    return i, j
        return -1, -1

    def check_board(self, board, row, col, num):
        for i in range(9):
            if i != row and board[i][col] == num:
                return False
            if i != col and board[row][i] == num:
                return False

        # 检查9宫格
        row_9 = row / 3 * 3
        col_9 = col / 3 * 3
        for i in range(3):
            for j in range(3):
                if (row_9 + i != row or col_9 + j != col) and board[row_9+i][col_9+j] == num:
                    return False
        return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Solution().solveSudoku(board)
assert board == [
    ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ['3', '4', '5', '2', '8', '6', '1', '7', '9']
]