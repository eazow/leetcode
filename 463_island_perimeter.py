class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        gridRows = len(grid)
        if gridRows == 0:
            return 0
        gridCols = len(grid[0])
        for i in range(gridRows):
            for j in range(gridCols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j]:
                        perimeter -= 1
                    if j > 0 and grid[i][j-1]:
                        perimeter -= 1
                    if i+1 < gridRows and grid[i+1][j]:
                        perimeter -= 1
                    if j+1 < gridCols and grid[i][j+1]:
                        perimeter -= 1

        return perimeter

assert Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16