class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        l,r = 0, 1
        
        max_profit = 0
        while l < r and r < len(prices) :
            
            if prices[r] < prices[l]  :
                l = r
                r = l+1

                if l == r or r >= len(prices) :
                    break

            
            profit = prices[r] - prices [l]
            max_profit = max(profit,max_profit)
            r += 1

        print(max_profit)
        return max_profit    




        
        
        '''
        max_profit = 0
        for left in range(len(prices)) :
            
            if left > 0 and prices[left] > prices[left-1]:
                continue
            
            for right in range(left+1,len(prices)):
                profit = prices[right] - prices[left]
                max_profit = max(max_profit,profit)
        
        print(max_profit)        
        return max_profit'''






        