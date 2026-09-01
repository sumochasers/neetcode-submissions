class Solution:
    def getMinCoinsDfs(self, i, coins, amount, cache):
        
        if amount == 0 :
            return 0
        if amount < 0 or i >= len(coins) :
            return float('inf')
        if (i, amount) in cache :
            return cache[(i, amount)]
        

        numCoins = min(1 + self.getMinCoinsDfs(i, coins, amount - coins[i], cache), self.getMinCoinsDfs(i + 1, coins, amount, cache))
        cache[(i, amount)] = numCoins
        return cache[(i, amount)]

    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        minNumCoins =  self.getMinCoinsDfs(0, coins, amount, cache)
        if minNumCoins == float('inf'):
            return -1
        else :
            return minNumCoins
        