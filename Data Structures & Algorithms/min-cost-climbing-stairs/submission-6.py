class Solution:
    cache = {}
    def getCostDfs(self, i, cost, cache):
        if i >= len(cost) :
            return 0
        if i in cache :
            return cache[i]
        cache[i] = cost[i] + min(self.getCostDfs( i + 1 , cost, cache) , self.getCostDfs( i + 2 , cost, cache) )
        return cache[i]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        return min(self.getCostDfs(0, cost, cache), self.getCostDfs(1, cost, cache))