class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if click[0] + i < 0 or click[0] + i >= len(board) or \
                        click[1] + j < 0 or click[1] + j >= len(board[0]):
                        continue
                    if board[click[0] + i][click[1] + j] == 'M':
                        count += 1

            if count > 0:
                board[click[0]][click[1]] = str(count)
            else:
                board[click[0]][click[1]] = 'B'
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i == 0 and j == 0) or click[0] + i < 0 or click[0] + i >= len(board) or \
                            click[1] + j < 0 or click[1] + j >= len(board[0]):
                            continue
                        elif board[click[0] + i][click[1] + j] == 'E':
                            self.updateBoard(board, [click[0] + i, click[1] + j])

        return board

board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]
result_board = [['B', '1', 'E', '1', 'B'],
                ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']]

assert Solution().updateBoard(board, [3, 0]) == result_board
