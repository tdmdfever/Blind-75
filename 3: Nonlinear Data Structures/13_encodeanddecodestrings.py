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
    res = s[1:len(s) - 1].split(',')
    return res