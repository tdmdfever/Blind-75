"""
Given a string, determine the number of palindromic substrings present in it.

A palindromic substring is a sequence of characters that reads the same 
forwards and backward. The substring can be of any length, including 1.

Example 1:
Input: "racecar"
Expected Output: 10
Justification: The palindromic substrings are "r", "a", "c", "e", "c", "a", "r", "cec", "aceca", "racecar".

Example 2:
Input: "noon"
Expected Output: 6
Justification: The palindromic substrings are "n", "o", "o", "n", "oo", "noon".

Example 3:
Input: "apple"
Expected Output: 6
Justification: The palindromic substrings are "a", "p", "p", "l", "e", "pp".
"""

def count_palindromes_1(s: str) -> int:
    if not s:
        return 0
    palindromes = len(s)
        
    def check_palindrome(s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    indexes = {}
    for i in range(len(s)):
        if s[i] in indexes:
            for j in indexes[s[i]]:
                if check_palindrome(s[j:i+1]):
                    palindromes += 1

        if s[i] not in indexes:
            indexes[s[i]] = []
        indexes[s[i]].append(i)

    return palindromes

def count_palindromes_2(s: str) -> int:
    palindromes = 0

    def check_palindromes(left, right):
        nonlocal palindromes
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        check_palindromes(i, i)
        check_palindromes(i, i + 1)

    return palindromes

# Test:
print(count_palindromes_1("racecar"))