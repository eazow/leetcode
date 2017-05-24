class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        total = duration
        for i in range(0, len(timeSeries)-1):
            total += min(timeSeries[i+1]-timeSeries[i], duration)

        return total

assert Solution().findPoisonedDuration([1,4], 2) == 4
assert Solution().findPoisonedDuration([1,2], 2) == 3
assert Solution().findPoisonedDuration([], 100) == 0