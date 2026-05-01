class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L ,R = 0, len(numbers) - 1

        while R > L:
            sum_num = numbers[R] + numbers[L]
            if sum_num > target:
                R -= 1
            elif sum_num < target:
                L += 1
            else:
                return [L + 1, R + 1]
                
