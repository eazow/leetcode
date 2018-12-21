# -*- coding:utf-8 -*-


class Solution(object):
    def solveSudoku(self, board):
        """
        :param board: List[List[int]]
        :return: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)


    def solve(self, board):
        self.print_board(board)

        # import time
        # time.sleep(10)
        row, col = self.get_empty_cell(board)

        if row == -1:
            return True
        else:
            for num in "123456789":
                if self.check_board(board, row, col, num):
                    board[row][col] = num
                    self.print_board(board)
                    # 关键点
                    self.solve(board)

        return False

    def print_board(self, board):
        for row in board:
             print row

        print ""

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


Solution().solveSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
])