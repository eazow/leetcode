class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        bricks_map = {}
        for row in wall:
            sum = 0
            col = 0
            for brick in row:
                sum += brick
                if sum in bricks_map:
                    bricks_map[sum] += 1
                elif col != len(row) - 1:
                    bricks_map[sum] = 1
                col += 1

        height = len(wall)
        least = height
        for brick in bricks_map:
            least = min(height - bricks_map.get(brick), least)

        return least

assert Solution().leastBricks([
    [1,2,2,1],
    [3,1,2],
    [1,3,2],
    [2,4],
    [3,1,2],
    [1,3,1,1]]) == 2