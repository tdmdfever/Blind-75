"""
Design a class to calculate the median of a stream of numbers. The class 
should have the following two methods:

insert_num(int num): stores the number in the class
find_median(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the two middle numbers.

Example 1:
1. insert_num(3)
2. insert_num(1)
3. find_median() -> output: 2.0
4. insert_num(5)
5. find_median() -> output: 3.0
6. insert_num(4)
7. find_median() -> output: 3.5
"""

from heapq import *

# With 3.14+ (including max-heap):

class Solution: 

    def __init__(self):
        self.low = [] # max-heap containing lower half of data
        self.high = [] # min-heap containing upper half of data

    def insert_num(self, num):
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

    def find_median(self):
        if len(self.low) == len(self.high):
            return (self.low[0] + self.high[0])/2
        else:
            return float(self.low[0])

# Pre 3.14 (without max-heap):

class OldSolution: 

    def __init__(self):
        self.low = [] # max-heap containing lower half of data
        self.high = [] # min-heap containing upper half of data

    def insert_num(self, num):
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

    def find_median(self):
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0])/2
        else:
            return float(-self.low[0])

# Test:
test = Solution()
test.insert_num(3)
test.insert_num(1)
print(test.find_median())
test.insert_num(5)
print(test.find_median())
test.insert_num(4)
print(test.find_median())

test_old = OldSolution()
test_old.insert_num(3)
test_old.insert_num(1)
print(test_old.find_median())
test_old.insert_num(5)
print(test_old.find_median())
test_old.insert_num(4)
print(test_old.find_median())