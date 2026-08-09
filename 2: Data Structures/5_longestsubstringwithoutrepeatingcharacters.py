# Longest Substring Without Repeating Characters
def findLength(str1, k):
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

"""
print(findLength('aabbbbc', 3))
"""