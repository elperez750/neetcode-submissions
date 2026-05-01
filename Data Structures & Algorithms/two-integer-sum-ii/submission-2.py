class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) -1
        while p1 < p2:
            sum_of_pointers = numbers[p1] + numbers[p2]
            if sum_of_pointers < target:
                p1 += 1
            elif sum_of_pointers > target:
                p2 -= 1
            
            else:
                return [p1+1, p2+1]