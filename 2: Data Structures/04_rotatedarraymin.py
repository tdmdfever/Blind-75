"""
You have an array of length n, which was initially sorted in ascending order. 
This array was then rotated x times. It is given that 1 <= x <= n. For 
example, if you rotate [1, 2, 3, 4] array 3 times, resultant array is 
[2, 3, 4, 1].

Your task is to find the minimum element from this array. Note that the array 
contains unique elements.

You must write an algorithm that runs in O(logn) time.

Example 1:
Input: [8, 1, 3, 4, 5]
Expected Output: 1
Justification: The smallest number in the array is 1.

Example 2:
Input: [4, 5, 7, 8, 0, 2, 3]
Expected Output: 0
Justification: The smallest number in the array is 0.

Example 3:
Input: [7, 9, 12, 3, 4, 5]
Expected Output: 3
Justification: In this rotated array, the smallest number present is 3.
"""

def find_min(nums) -> int:
    if not nums:
        return None
    left, right = 0, len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if nums[right] >= nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
            
    return nums[left]

# Test:
print(find_min([3,4,5,1,2]))