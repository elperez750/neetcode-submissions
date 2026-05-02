class Solution:
    def climbStairs(self, n: int) -> int:
        way1, way2 = 1, 1
        for _ in range(n-1):
            temp = way2
            way2 = way1 + way2
            way1 = temp

        return way2            
            