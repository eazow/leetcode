class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        houses = sorted(houses)
        heaters = sorted(heaters)

        radius = 0
        for house in houses:
            index = self.binary_search(heaters, house)
            if house != heaters[index]:
                temp_radius = abs(house - heaters[index])
                if index + 1 < len(heaters):
                    temp_radius = min(temp_radius, abs(house - heaters[index + 1]))
                radius = max(radius, temp_radius)

        return radius

    def binary_search(self, nums, num):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] < num:
                low = mid + 1
            elif nums[mid] > num:
                high = mid -1
            else:
                return mid
        return high if high > 0 else 0

assert Solution().findRadius([1, 2, 3], [2]) == 1
assert Solution().findRadius([1, 2, 3, 4], [1, 4]) == 1
assert Solution().findRadius([1], [1, 2, 3, 4]) == 0
assert Solution().findRadius([1, 2, 3, 5, 15], [2, 30]) == 13
assert Solution().findRadius([1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999], [499, 500, 501]) == 498
assert Solution().findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923], 
    [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]) == 161834419
