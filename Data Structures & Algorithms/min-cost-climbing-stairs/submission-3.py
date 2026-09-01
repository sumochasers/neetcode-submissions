class Solution:
    
    def dfs(self, index, cost, cache):
        
        if index >= len(cost) :
            return 0
        if cache[index] != -1 :
            return cache[index]
        
        cache[index] = cost[index] + min (self.dfs(index+1, cost, cache), self.dfs(index+2, cost, cache))
        return cache[index]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = [-1] * len(cost)
        self.dfs(0,cost, cache)
        return min(cache[0], cache[1])

        