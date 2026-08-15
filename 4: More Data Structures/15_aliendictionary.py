"""
There is a dictionary containing words from an alien language for which we
don't know the ordering of the letters.

Given a list of strings words from the alien language's dictionary. All strings
in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in
lexicographically increasing order by the new language's rules.

It is given that the input is a valid dictionary and there exists an ordering
among its letters.

Example 1:
Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically
by the rules of the alien language, so
from the given words we can conclude the following ordering
among its characters:

1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

From the above two points, we can conclude that the correct
character order is: "bac"

Example 2:
Input: Words: ["cab", "aaa", "aab"]
Output: cab
Explanation: From the given words we can conclude the following
ordering among its characters:

1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'

From the above two points, we can conclude that the correct character order is: "cab"

Example 3:
Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
Output: ywxz
Explanation: From the given words we can conclude the following
ordering among its characters:

1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'

From the above five points, we can conclude that the correct
character order is: "ywxz"
"""

from collections import deque

def find_order_kahn(words):
    unique_chars = set(''.join(words))
    adjacency = {char: [] for char in unique_chars}
    degree = {char: 0 for char in unique_chars}

    for i in range(1,len(words)):
        prev_word, curr_word = words[i-1], words[i]

        if len(prev_word) > len(curr_word) and prev_word.startswith(curr_word):
            return ""

        for char1, char2 in zip(prev_word, curr_word):
            if char1 != char2:
                adjacency[char1].append(char2)
                degree[char2] += 1
                break



    queue = deque([char for char in degree if degree[char] == 0])
    order = []
    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in adjacency[char]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(order) if len(order) == len(adjacency) else ""

# Test:
print(find_order_kahn(["ba", "bc", "ac", "cab"]))
print(find_order_kahn(["cab", "aaa", "aab"]))
print(find_order_kahn(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))

# def find_order_dfs(words):
#     unique_chars = set(''.join(words))
#     neighbor = {char: [] for char in unique_chars}

#     for i in range(1,len(words)):
#         w1, w2 = words[i-1], words[i]

#         if len(w1) > len(w2) and w1.startswith(w2):
#             return ""

#         for c1, c2 in zip(w1, w2):
#             if c1 != c2:
#                 neighbor[c1].append(c2)
#                 break

#     queue = deque([char for char in degree if degree[char] == 0])
#     order = []
#     while queue:
#         char = queue.popleft()
#         order.append(char)
#         for neighbor in neighbor[char]:
#             degree[neighbor] -= 1
#             if degree[neighbor] == 0:
#                 queue.append(neighbor)

#     return ''.join(order) if len(order) == len(neighbor) else ""