"""
Given an integer array, find the contiguous subarray (at least one number 
in it) that has the maximum product. Return this maximum product.

Example 1:
Input: [2,3,-2,4]
Expected Output: 6
Justification: The subarray [2,3] has the maximum product of 6.

Example 2:
Input: [-2,0,-1]
Expected Output: 0
Justification: The subarray [0] has the maximum product of 0.

Example 3:
Input: [-2,3,2,-4]
Expected Output: 48
Justification: The subarray [-2,3,2,-4] has the maximum product of 
48.
"""

def max_product(nums):
    best_product = current_max = current_min = nums[0]
    for num in nums[1:]:
        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        best_product = max(best_product, current_max)

    return best_product

# Test:
print(max_product([2,3,-2,4]))