"""
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, using all the original letters exactly once.

Example 1:
Input: s = "listen", t = "silent"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Example 3:
Input: s = "hello", t = "world"
Output: false
"""

def is_anagram_1(s, t):
    return sorted(s) == sorted(t)

def is_anagram_2(s, t):
    if len(s) != len(t):
        return False
    
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in t:
        freq[char] = freq.get(char, 0) - 1
    
    return all(freq_ct == 0 for freq_ct in freq.values())

# Test:
print(is_anagram_1("listen", "silent"))
print(is_anagram_1("abc", "abb"))