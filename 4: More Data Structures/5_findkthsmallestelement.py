import random

def findKthSmallestNumber(nums, k):
    index = random.randint(0, len(nums) - 1)
    pivot = nums[index]
    
    left, mid, right = [], [], []
    for i in range(len(nums)):
        if nums[i] == pivot:
            mid.append(nums[i])
        if nums[i] < pivot:
            left.append(nums[i])
        elif nums[i] > pivot:
            right.append(nums[i])
    
    if k <= len(left):
        return findKthSmallestNumber(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    elif k > len(left) + len(mid):
        return findKthSmallestNumber(right, k - (len(left) + len(mid))) 