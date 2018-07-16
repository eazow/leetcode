class Solution(object):
    def cmp_time(self, time1, time2):
        hour1, minute1 = map(int, time1.split(":"))
        hour2, minute2 = map(int, time2.split(":"))
        if hour1 > hour2:
            return 1
        elif hour1 < hour2:
            return -1
        else:
            return cmp(minute1, minute2)

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time_points = sorted(timePoints, self.cmp_time)

        time_point1 = time_points[0]
        time_point2 = time_points[-1]
        hour1, minute1 = map(int, time_point1.split(":"))
        hour2, minute2 = map(int, time_point2.split(":"))

        difference = hour1 * 60 + minute1 + (23 - hour2) * 60 + 60 - minute2
        for i in xrange(len(time_points) - 1):
            time_point1 = time_points[i]
            time_point2 = time_points[i + 1]

            hour1, minute1 = map(int, time_point1.split(":"))
            hour2, minute2 = map(int, time_point2.split(":"))
            difference = min(
                difference,
                (hour2 - hour1 - 1) * 60 + minute2 + 60 - minute1 if hour2 > hour1 else minute2 - minute1
            )

        return difference


assert Solution().findMinDifference(["00:00", "23:59", "00:00"]) == 0
assert Solution().findMinDifference(["23:59", "00:00", "10:00", "9:10"]) == 1
assert Solution().findMinDifference(["12:12", "12:13", "00:12", "00:13"]) == 1