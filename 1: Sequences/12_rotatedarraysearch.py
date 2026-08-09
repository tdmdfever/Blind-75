"""
Given an array of numbers which is sorted in ascending order and also 
rotated by some arbitrary number, find if a given 'key' is present in it.

Write a function to return the index of the 'key' in the rotated array. If the 
'key' is not present, return -1. You can assume that the given array does not have any duplicates.

Note: You need to solve the problem in O(logn) time complexity.

Example 1:
Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Example 2:
Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
"""

def rotated_search(arr, key):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < key <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
      
    return -1

# Test:
print(rotated_search([10, 15, 1, 3, 8], 15))