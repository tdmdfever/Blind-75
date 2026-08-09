# Find top K frequent numbers

def find_top_k_frequent_numbers(nums, k):
    topNumbers = []
    ledger = {}
    for i in range(len(nums)):
        ledger[nums[i]] = ledger.get(nums[i], 0) + 1

    return sorted(ledger, key = lambda x: ledger[x], reverse = True)[:k]

"""
print(findTopKFrequentNumbers([1, 3, 5, 12, 11, 12, 11], 2))
"""