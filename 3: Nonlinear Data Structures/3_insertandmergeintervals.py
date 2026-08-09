# Insert and merge interval

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

"""
# Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
interval1, interval2, interval3, new_interval = Interval(1, 3), Interval(5, 7), Interval(8, 12), Interval(4, 10)
intervals = [interval1, interval2, interval3]
for interval in insert(intervals, new_interval):
    print(f"({interval.start}, {interval.end})")
"""