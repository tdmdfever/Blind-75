### from 4_validanagram.py ###
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
###


def group_anagrams(strs):
    grouped_anagrams = [[strs[0]]]

    for s in strs:
        found = False
        for group in grouped_anagrams:
            if is_anagram_2(s, group[0]):
                group.append(s)
                found = True
        if not found:
            grouped_anagrams.append([s])

    return grouped_anagrams