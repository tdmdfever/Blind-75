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

def find_length(str1, k):
    max_length = 0
    left = right = 0
    ledger = {}
      
    while right < len(str1):
        ledger[str1[right]] = ledger.get(str1[right], 0) + 1

        while (right - left + 1) - max(ledger.values()) > k:
            ledger[str1[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length

# Test:
print(find_length('aabbbbc', 3))