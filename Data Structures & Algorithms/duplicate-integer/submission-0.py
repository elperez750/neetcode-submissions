class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i in range(len(nums)):
            if nums[i] in duplicates:
                return True
            else:
                duplicates[nums[i]] = i

        return False