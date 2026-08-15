"""
Given a list of strings, your task is to develop two functions: one that 
encodes the list of strings into a single string, and another that decodes the 
resulting single string back into the original list of strings. It is crucial that 
the decoded list is identical to the original one.

It is given that you can use any encoding technique to encode list of string 
into the single string.

Example 1:
Input: ["apple", "banana"]
Expected Output: ["apple", "banana"]
Justification: When we encode the input strings ["apple", "banana"], 
we get a single encoded string. Decoding this encoded string should 
give us the original list ["apple", "banana"].

Example 2:
Input: ["sun", "moon", "stars"]
Expected Output: ["sun", "moon", "stars"]
Justification: After encoding the input list, decoding it should bring 
back the original list.

Example 3:
Input: ["Hello123", "&*^%"]
Expected Output: ["Hello123", "&*^%"]
Justification: Regardless of the content of the string (special 
characters, numbers, etc.), decoding the encoded list should 
reproduce the original list.
"""

def encode(strs):
    if not strs:
        return "[]"
    encoded = "[" + strs[0]
        
    for string in strs[1:]:
        encoded += ',' + string
    encoded += ']'
    return encoded
    
def decode(s):
    if not s or s == '[]':
        return []
    decoded = s[1:len(s) - 1].split(',')
    return decoded

# Test:
strs = ['apple', 'banana']
encoded = encode(strs)
decoded = decode(encoded)
print(encoded)
for string in decoded:
    print(string)