class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            if not diff or nums[i] not in diff:
                diff[target - nums[i]] = i
               
            else:
                return [diff[nums[i]], i]  

        