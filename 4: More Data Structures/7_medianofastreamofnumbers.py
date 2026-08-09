from heapq import *

# With 3.14+ (including max-heap):

class Solution: 

    def __init__(self):
        self.low = [] # max-heap containing lower half of data
        self.high = [] # min-heap containing upper half of data

    def insertNum(self, num):
        if not self.low and not self.high:
            heappush_max(self.low, num)
        else:
            if self.low and num <= self.low[0]:
                heappush_max(self.low, num)
            else:
                heappush(self.high, num)
    
    # balancing
        if len(self.low) > len(self.high) + 1:
            heappush(self.high, heappop_max(self.low))
        elif len(self.high) > len(self.low):
            heappush_max(self.low, heappop(self.high))

    def findMedian(self):
        if len(self.low) == len(self.high):
            return (self.low[0] + self.high[0])/2
        else:
            return self.low[0]

# Pre 3.14 (without max-heap):

class oldSolution: 

    def __init__(self):
        self.low = [] # max-heap containing lower half of data
        self.high = [] # min-heap containing upper half of data

    def insertNum(self, num):
        if not self.low and not self.high:
            heappush(self.low, -num)
        else:
            if self.low and num <= -self.low[0]:
                heappush(self.low, -num)
            else:
                heappush(self.high, num)
    
        # balancing
        if len(self.low) > len(self.high) + 1:
            heappush(self.high, -heappop(self.low))
        elif len(self.high) > len(self.low):
            heappush(self.low, -heappop(self.high))

    def findMedian(self):
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0])/2
        else:
            return -self.low[0]