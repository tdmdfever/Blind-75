"""
Design a class to calculate the median of a stream of numbers. The class 
should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the two middle numbers.

Example 1:
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2.0
4. insertNum(5)
5. findMedian() -> output: 3.0
6. insertNum(4)
7. findMedian() -> output: 3.5
"""

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
            return float(self.low[0])

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
            return float(-self.low[0])

# Test:
test = Solution()
test.insertNum(3)
test.insertNum(1)
print(test.findMedian())
test.insertNum(5)
print(test.findMedian())
test.insertNum(4)
print(test.findMedian())

test_old = oldSolution()
test_old.insertNum(3)
test_old.insertNum(1)
print(test_old.findMedian())
test_old.insertNum(5)
print(test_old.findMedian())
test_old.insertNum(4)
print(test_old.findMedian())