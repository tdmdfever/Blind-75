"""
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the 
Kth distinct element.

Example 1:
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two 
smaller numbers are [1, 2].

Example 2:
Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three 
smaller numbers are [1, 2, 5].

Example 3:
Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two 
small numbers are [5, -1].
"""

import random

def find_kth_smallest_number(nums, k):
    index = random.randint(0, len(nums) - 1)
    pivot = nums[index]
    
    left, mid, right = [], [], []
    for i in range(len(nums)):
        if nums[i] == pivot:
            mid.append(nums[i])
        if nums[i] < pivot:
            left.append(nums[i])
        elif nums[i] > pivot:
            right.append(nums[i])
    
    if k <= len(left):
        return find_kth_smallest_number(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    elif k > len(left) + len(mid):
        return find_kth_smallest_number(right, k - (len(left) + len(mid))) 

# Test:
print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3))