class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        prev_ptr = 0
        next_ptr = 1
        max_profit = 0

        while next_ptr < len(prices):
            if prices[prev_ptr] <= prices[next_ptr]:
                if prices[next_ptr] - prices[prev_ptr] > max_profit:
                    max_profit = prices[next_ptr] - prices[prev_ptr]
                next_ptr += 1
            
            else:
                prev_ptr = next_ptr
                next_ptr += 1
            


        return max_profit


