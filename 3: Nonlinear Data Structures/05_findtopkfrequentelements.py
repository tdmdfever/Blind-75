"""
Given an unsorted array of numbers, find the top 'K' frequently occurring 
numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' appeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice; all other numbers appeared once.
"""

def find_top_k_frequent_numbers(nums, k):
    topNumbers = []
    ledger = {}
    for i in range(len(nums)):
        ledger[nums[i]] = ledger.get(nums[i], 0) + 1

    return sorted(ledger, key = lambda x: ledger[x], reverse = True)[:k]


# Test
print(find_top_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2))