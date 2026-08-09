def findMin(nums) -> int:
    if not nums:
        return None
    left, right = 0, len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if nums[right] >= nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
            
    return nums[left]