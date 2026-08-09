"""
Given an array, find the length of the smallest subarray in it which when 
sorted will sort the whole array.

Example 1:
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] 
to make the whole array sorted

Example 2:
Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] 
to make the whole array sorted

Example 3:
Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Example 4:
Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
"""

def minimum_window_sort(arr):
    left = 0
    right = len(arr) - 1

    while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
        left += 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    
    if left == len(arr) - 1:
        return 0
    
    min_val = min(arr[left:right + 1])
    max_val = max(arr[left: right + 1])

    while left > 0 and arr[left - 1] > min_val:
        left -= 1
    while right < len(arr) - 1 and arr[right + 1] < max_val:
        right += 1

    return right - left + 1

# Test:
print(minimum_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(minimum_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(minimum_window_sort([1, 2, 3]))
print(minimum_window_sort([3, 2, 1]))