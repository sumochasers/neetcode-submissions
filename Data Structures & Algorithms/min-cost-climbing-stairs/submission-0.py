class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dfs(current):
            
            if current >= len(cost) :
                return 0
            
            return cost[current] + min(dfs(current+1),dfs(current+2))  

        return min(dfs(0),dfs(1))



        