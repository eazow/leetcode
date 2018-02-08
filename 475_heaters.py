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
        radius = abs(houses[0] - heaters[0])
        while i < len(houses) and j < len(heaters):
            if abs(houses[i] - heaters[j]) <= radius:
                i += 1
            elif j + 1 < len(heaters):
                if abs(houses[i] - heaters[j+1]) <= radius:
                    i += 1
                    j += 1
                elif abs(houses[i] - heaters[j]) <= abs(houses[i] - heaters[j+1]):
                    radius = abs(houses[i] - heaters[j])
                    i += 1
                else:
                    while j + 1 < len(heaters) and abs(houses[i] - heaters[j]) > abs(houses[i] - heaters[j+1]):
                        temp_radius = abs(houses[i] - heaters[j+1])
                        j += 1
                    if temp_radius > radius:
                        radius = temp_radius
                    i += 1
            else:
                radius = abs(houses[i] - heaters[j])
                i += 1

        return radius

assert Solution().findRadius([1, 2, 3], [2]) == 1
assert Solution().findRadius([1, 2, 3, 4], [1, 4]) == 1
assert Solution().findRadius([1], [1, 2, 3, 4]) == 0
assert Solution().findRadius([1, 2, 3, 5, 15], [2, 30]) == 13
assert Solution().findRadius([1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999], [499, 500, 501]) == 498
print Solution().findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923], 
    [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612])
