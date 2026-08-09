# Check for duplicates
def contains_duplicate_1(nums):
      seen = set()
      for num in nums:
        if num in seen:
          return True
        seen.add(num)
      return False

def contains_duplicate_2(nums):
   return len(nums) != len(set(nums))

def contains_duplicate_solution(nums):
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]: # if any two elements are the same, return true
          return True
    return False # if no duplicates are found, return false
