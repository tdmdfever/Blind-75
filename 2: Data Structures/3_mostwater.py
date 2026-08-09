# Container with most water
def maxArea(arr):
    left, right = 0, len(arr) - 1
    maxArea = 0
    while left < right:
        maxArea = max(maxArea, (right - left) * min(arr[left], arr[right]))
        if arr[left] <= arr[right]:
            left += 1
        else:
            right -= 1
        
    return maxArea