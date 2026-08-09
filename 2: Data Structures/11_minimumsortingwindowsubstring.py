# Minimum Sorting Window Substring

def minimum_window_sort(arr):
    left = 0
    right = len(arr) - 1

    while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
        left += 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    
    if left == len(arr) - 1:
        return 0
    
    min_val = min(arr[left:right + 1])
    max_val = max(arr[left: right + 1])

    while left > 0 and arr[left - 1] > min_val:
        left -= 1
    while right < len(arr) - 1 and arr[right + 1] < max_val:
        right += 1

    return right - left + 1
