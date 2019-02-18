# -*- coding:utf-8 -*-

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return "Interval: %s, %s" % (self.start, self.end)


def cmp_interval(interval1, interval2):
    return -1 if interval1.start <= interval2.start else 1


class Solution(object):
    def insert(self, intervals, new_interval):
        """
        :param intervals: List[Interval]
        :param new_interval: Interval
        :return: List[Interval]
        """
        intervals.append(new_interval)
        intervals = sorted(intervals, cmp_interval)

        return self.merge(intervals)

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
                intervals[i+1] = Interval(start, max(end, end_next))

            i += 1

        merge_intervals.append(intervals[i])

        return merge_intervals


assert Solution().insert([Interval(1, 3), Interval(6, 9)], Interval(2, 5)) == [Interval(1, 5), Interval(6, 9)]