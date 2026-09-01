class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        cur_min = prices[0]
        r = 1
        max_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit,profit)
            if prices[r] < cur_min :
                l = r
                cur_min = prices[r]
            r += 1
        return max_profit