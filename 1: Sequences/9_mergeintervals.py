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