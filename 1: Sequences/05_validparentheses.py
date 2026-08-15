"""
Determine if an input string containing only the characters '(', ')', '{', '}', '[', and 
']' is valid. A string is considered valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Each close bracket has a corresponding open bracket of the same type.

Example 1:
Input: "(]"
Expected Output: false
Justification: The opening parenthesis '(' is not closed by its corresponding closing parenthesis.

Example 2:
Input: "{[]}"
Expected Output: true
Justification: The string contains pairs of opening and closing brackets in the correct order.

Example 3:
Input: "[{]}"
Expected Output: false
Justification: The opening square bracket '[' is closed by a curly brace '}', which is incorrect.
"""

def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs:
            top = stack.pop() if stack else ' '
            if pairs[char] != top:
                return False
        else:
            stack.append(char)

    return not stack

# Test:
print(is_valid("()[]{}"))
print(is_valid("([)]"))