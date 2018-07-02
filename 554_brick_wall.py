class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        empty_count_map = {}
        for row in wall:
            sum = 0
            col = 0
            for brick in row:
                sum += brick
                if sum in empty_count_map:
                    empty_count_map[sum] += 1
                elif col != len(row) - 1:
                    empty_count_map[sum] = 1
                col += 1

        max_count = 0
        for empty in empty_count_map:
            count = empty_count_map.get(empty)
            max_count = max(max_count, count)

        return len(wall) - max_count


assert Solution().leastBricks([
    [1,2,2,1],
    [3,1,2],
    [1,3,2],
    [2,4],
    [3,1,2],
    [1,3,1,1]]) == 2