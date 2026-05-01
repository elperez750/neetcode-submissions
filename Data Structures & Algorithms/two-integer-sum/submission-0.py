class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}
        for i in range(len(nums)):
            number_to_find = target - nums[i]
            if number_to_find in seen_numbers:
                return [seen_numbers[number_to_find], i]
            else:
                seen_numbers[nums[i]] = i

    