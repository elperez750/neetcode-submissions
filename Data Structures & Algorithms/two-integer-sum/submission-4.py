class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(len(nums)):
            if nums[i] in values:
                return [values[nums[i]], i]
            else:
                values[target - nums[i]] = i

        
        