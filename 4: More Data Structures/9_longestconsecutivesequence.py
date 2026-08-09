
class Solution:
    def longestConsecutive(self, nums):
        longest_sequence = 1
        nums.sort()
        current_longest = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_longest += 1
            else:
                current_longest = 1
            longest_sequence = max(longest_sequence, current_longest)
            

        return longest_sequence

