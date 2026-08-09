"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums= [1, 2, 3, 4]
Output: false  
Explanation: There are no duplicates in the given array.

Example 2:
Input: nums= [1, 2, 3, 1]
Output: true  
Explanation: '1' is repeating.

Example 3:
Input: nums= [3, 2, 6, -1, 2, 1]
Output: true  
Explanation: '2' is repeating.
"""

def contains_duplicate_1(nums):
      seen = set()
      for num in nums:
        if num in seen:
          return True
        seen.add(num)
      return False

def contains_duplicate_2(nums):
   return len(nums) != len(set(nums))

def contains_duplicate_solution(nums):
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]: # if any two elements are the same, return true
          return True
    return False # if no duplicates are found, return false

# Test:
print(contains_duplicate_solution([1, 2, 3, 4])) 
print(contains_duplicate_solution([1, 2, 3, 1]))