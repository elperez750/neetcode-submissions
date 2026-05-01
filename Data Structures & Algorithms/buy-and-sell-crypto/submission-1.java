class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int max = 0;
        if (prices.length == 1) {
            return 0;
        }
        

        while (right < prices.length) {
            if(prices[left] >= prices[right]) {
                left = right;
            }

            else {
                if (prices[right] - prices[left] > max) {
                    max = prices[right] - prices[left];
                }
            }

            right += 1;
        }   

        return max;

    }
}
