# -*- coding:utf-8 -*-

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return "Interval: %s, %s" % (self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :param intervals: List[Interval]
        :return: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        i = 0
        merge_intervals = []
        while i < len(intervals) - 1:
            interval = intervals[i]
            interval_next = intervals[i+1]
            start = interval.start
            end = interval.end

            start_next = interval_next.start
            end_next = interval_next.end

            if end < start_next:
                merge_intervals.append(interval)
            elif start_next <= end:
                intervals[i+1] = Interval(start, end_next)

            i += 1

        merge_intervals.append(intervals[i])

        for interval in merge_intervals:
            print interval
        return merge_intervals


assert Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]) == \
       [Interval(1, 6), Interval(8, 10), Interval(15, 18)]