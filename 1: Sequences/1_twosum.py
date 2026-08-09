# TwoSum
def two_sum(nums, target):
    # ToDO: Write Your Code Here.
    for i, num in enumerate(nums):
        if target - num != num and target - num in nums:
            first = i
            for j, number in enumerate(nums):
                if num + number == target:
                    second = j
                    break
            break
        
    return [first, second]

def two_sum_solution(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict.keys():
            return [num_dict[complement], i]
        else:
            num_dict[num] = i

print(two_sum([3, 2, 4], 6))
print(two_sum([-1, -2, -3, -4, -5], -8))
print(two_sum([10, 15, 21, 25, 30], 45))

print(two_sum_solution([3, 2, 4], 6))
print(two_sum_solution([-1, -2, -3, -4, -5], -8))
print(two_sum_solution([10, 15, 21, 25, 30], 45))