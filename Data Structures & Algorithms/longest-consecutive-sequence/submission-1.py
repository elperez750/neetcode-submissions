class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_range = 0

        nums = set(nums)
        for number in nums:
            current_range = 0
            if number - 1 not in nums:
                current_range += 1
                next_number = number + 1
                while next_number in nums:
                    next_number += 1
                    current_range += 1
                longest_range = max(longest_range, current_range)
        
        return longest_range
