class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X' and ((i > 0 and board[i-1][j]!='X') or i==0) and ((j > 0 and board[i][j-1]!='X') or j==0):
                    count += 1

        return count

assert Solution().countBattleships(["X..X","...X","...X"]) == 2
assert Solution().countBattleships(["...X","XXXX","...X"]) == 2