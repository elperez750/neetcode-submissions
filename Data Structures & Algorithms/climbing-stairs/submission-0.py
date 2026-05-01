class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n):
            if n == 2:
                return 2
            if n == 1:
                return 1

            else:
                return dp(n-1) + dp(n-2)
        return dp(n)        
