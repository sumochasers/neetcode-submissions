class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for left in range(len(prices)) :
            
            if left > 0 and prices[left] > prices[left-1]:
                continue
            
            for right in range(left+1,len(prices)):
                profit = prices[right] - prices[left]
                max_profit = max(max_profit,profit)
        
        print(max_profit)        
        return max_profit






        