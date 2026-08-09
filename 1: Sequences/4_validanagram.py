# Check for anagram
def is_anagram_1(s, t):
    return sorted(s) == sorted(t)

def is_anagram_2(s, t):
    if len(s) != len(t):
        return False
    
    freq = {}

    for i in s:
        freq[i] = freq.get(i, 0) + 1
    
    for j in t:
        freq[j] = freq.get(j, 0) - 1
    
    return all(freq_ct == 0 for freq_ct in freq.values())