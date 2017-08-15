class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for point_i in points:
            distance_map = {}
            for point_j in points:
                distance = (point_i[0] - point_j[0]) * (point_i[0] - point_j[0]) + \
                           (point_i[1] - point_j[1]) * (point_i[1] - point_j[1])
                distance_map[distance] = distance_map.get(distance, 0) + 1

            for distance in distance_map:
                count = distance_map[distance]
                result += count * (count - 1)

        return result

assert Solution().numberOfBoomerangs([[0,0], [1,0], [2,0]]) == 2