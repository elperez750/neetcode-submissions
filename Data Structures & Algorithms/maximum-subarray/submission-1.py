class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -1000000
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i > j:
                    continue
                else:
                    sub_array_sum = sum(nums[i:j+1])
                    if sub_array_sum > max_sum:
                        max_sum = sub_array_sum
        return max_sum

                




