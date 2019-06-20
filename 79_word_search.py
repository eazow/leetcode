# -*- coding:utf-8 -*-

class Solution(object):
    def exist(self, board, word):
        """
        :param board: List[List[str]]
        :param word: str
        :return: bool
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return word is None or word == ""
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
        
    def dfs(self, board, row, col, word):
        if len(word) == 0:
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[0]:
            return False

        board[row][col] = "#"
        result = self.dfs(board, row+1, col, word[1:]) or \
            self.dfs(board, row-1, col, word[1:]) or \
            self.dfs(board, row, col-1, word[1:]) or \
            self.dfs(board, row, col + 1, word[1:])
        board[row][col] = word[0]
        return result


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
assert Solution().exist(board, "ABCCED") == True
assert Solution().exist(board, "SEE") == True
assert Solution().exist(board, "ABCB") == False