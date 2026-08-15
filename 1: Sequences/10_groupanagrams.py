"""
Given a list of strings, the task is to group the anagrams together.

An anagram is a word or phrase formed by rearranging the letters of 
another, such as "cinema", formed from "iceman"

You can return the answer in any order.

Example 1:
Input: ["dog", "god", "hello"]
Output: [["dog", "god"], ["hello"]]
Justification: "dog" and "god" are anagrams, so they are grouped together. 
"hello" does not have any anagrams in the list, so it is in its 
own group.

Example 2:
Input: ["listen", "silent", "enlist"]
Output: [["listen", "silent", "enlist"]]
Justification: All three words are anagrams of each other, so they are
grouped together.

Example 3:
Input: ["abc", "cab", "bca", "xyz", "zxy"]
Output: [["abc", "cab", "bca"], ["xyz", "zxy"]]
Justification: "abc", "cab", and "bca" are anagrams, as are "xyz" and "zxy".
"""

### from 04_validanagram.py ###
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
###


def group_anagrams(strs):
    grouped_anagrams = [[strs[0]]]

    for word in strs:
        found = False
        for group in grouped_anagrams:
            if is_anagram_2(word, group[0]):
                group.append(word)
                found = True
        if not found:
            grouped_anagrams.append([word])

    return grouped_anagrams

# Test
print(group_anagrams(["dog", "god", "hello"]))