"""
Given an unsorted array of integers, find the length of the longest 
consecutive sequence of numbers in it. A consecutive sequence means the 
numbers in the sequence are contiguous without any gaps. For instance, 1, 
2, 3, 4 is a consecutive sequence, but 1, 3, 4, 5 is not.

Example 1:
Input: [10, 11, 14, 12, 13]
Output: 5
Justification: The entire array forms a consecutive sequence from 10 
to 14.

Example 2:
Input: [3, 6, 4, 100, 101, 102]
Output: 3
Justification: There are two consecutive sequences, [3, 4] and 
[100,101,102]. The latter has a maximum length of 3.

Example 3:
Input: [4, 3, 6, 2, 5, 8, 4, 7, 0, 1]
Output: 9
Justification: The longest consecutive sequences here are [0, 1, 2, 3, 
4, 5, 6, 7, 8].

Example 4:
Input: [7, 8, 10, 11, 15]
Output: 2
Justification: The longest consecutive sequences here are [7,8] and 
[10,11], both of length 2.
"""