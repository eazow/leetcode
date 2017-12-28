class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        positions_map = {}
        for num in nums:
            if positions_map.has_key(num):
                positions_map[num].append(i)
            else:
                positions_map[num] = [i]
            i += 1

        result = 50000
        max_count = 0
        for num, positions in positions_map.items():
            if len(positions) > max_count:
                max_count = len(positions)
                result = positions[-1] - positions[0] + 1
            elif len(positions) == max_count:
                result = min(result, positions[-1] - positions[0] + 1)

        return result

assert Solution().findShortestSubArray([1, 2, 2, 3, 1]) == 2
assert Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6