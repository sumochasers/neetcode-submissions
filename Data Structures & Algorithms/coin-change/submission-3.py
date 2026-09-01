class Solution:
    
    def dfs(self, i, csum, coins, amount, cache):
        
        if (i, csum) in cache:
            return cache[(i, csum)]
        
        if i >= len(coins) or csum > amount :
            return 99999999
        
        if csum == amount :
            return 0
        
        with_this = 1 + self.dfs(i, csum+coins[i], coins, amount, cache)
        without_this = self.dfs(i+1, csum, coins, amount, cache)
        result = min(with_this, without_this)
        cache[(i, csum)] = result
        return result
        
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        result  = self.dfs(0, 0, coins, amount, cache)
        if result == 99999999 :
            return -1
        return result

        
        

        