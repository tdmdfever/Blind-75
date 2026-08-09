"""
Given a list of non-overlapping intervals sorted by their start time, insert a 
given interval at the correct position and merge all necessary intervals to 
produce a list that has only mutually exclusive intervals.

Example 1:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], 
we merged them into one [4,7].

Example 2:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & 
[8,12], we merged them into [4,12].

Example 3:
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], 
we merged them into one [1,4].
"""

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

def insert_intervals(intervals, new_interval):
    merged = []
    left_merged = False
    for i in range(len(intervals)):
        if intervals[i].end >= new_interval.start and new_interval.end >= intervals[i].start:
            if left_merged:
                merged[-1].end = max(new_interval.end, intervals[i].end)
            else:
                merged.append(Interval(min(new_interval.start, intervals[i].start), max(new_interval.end, intervals[i].end)))
                left_merged = True
        else:
            merged.append(intervals[i])
        
    return merged

# Test:
interval1, interval2, interval3, new_interval = Interval(1, 3), Interval(5, 7), Interval(8, 12), Interval(4, 10)
intervals = [interval1, interval2, interval3]
for interval in insert_intervals(intervals, new_interval):
    print(f"({interval.start}, {interval.end})")
