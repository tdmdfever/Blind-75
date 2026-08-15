"""
Given a string with lowercase letters only, if you are allowed to replace no 
more than 'k' letters with any letter, find the length of the longest substring 
having the same letters after replacement.

Example 1:
Input: str="aabccbb", k=2  
Output: 5  
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:
Input: str="abbcb", k=1  
Output: 4  
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:
Input: str="abccde", k=1  
Output: 3  
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

def find_longest_repeating_substring_length(s, k):
    max_length = 0
    left = right = 0
    char_counts = {}

    while right < len(s):
        char_counts[s[right]] = char_counts.get(s[right], 0) + 1

        while (right - left + 1) - max(char_counts.values()) > k:
            char_counts[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length

# Test:
print(find_longest_repeating_substring_length('aabbbbc', 3))