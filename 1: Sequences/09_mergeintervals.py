"""
Given a list of intervals, merge all the overlapping intervals to produce a list 
that has only mutually exclusive intervals.

Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] 
overlap, we merged them into one [1,5].

Example 2:
Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we 
merged them into one [5,9].

Example 3:
Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged 
them into one.
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"


def merge(intervals):
    if not intervals:
        return []

    sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
    merged_intervals = [Interval(sorted_intervals[0].start, sorted_intervals[0].end)]
    for interval in sorted_intervals[1:]:
        if merged_intervals[-1].end >= interval.start:
            merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)
        else:
            merged_intervals.append(Interval(interval.start, interval.end))

    return merged_intervals

# Test:
merged = merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)])
for merged_interval in merged:
    print(f"({merged_interval.start}, {merged_interval.end})")