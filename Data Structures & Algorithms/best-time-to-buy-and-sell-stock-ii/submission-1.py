class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}
        def dfs(i, bought):

            if i == len(prices) :
                return 0
            
            if (i, bought) in cache :
                return cache[(i, bought)]
            
            res = dfs(i + 1, bought)
            if bought :
                res = max(res, prices[i] + dfs(i + 1, False))
            else :
                res = max(res, -prices[i] + dfs(i + 1, True))

            cache[(i, bought)] = res
            return res
        
        return dfs(0, False)