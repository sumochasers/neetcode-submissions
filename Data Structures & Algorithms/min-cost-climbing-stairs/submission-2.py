class Solution:
    '''
    cost[0] + min_cost(1,2)
    cost[1] + min_cost(2,3)          

    '''
    def dfs(self, index, cost):
        if index >= len(cost):
            return 0
        return cost[index] + min(self.dfs(index+1, cost),self.dfs(index+2,cost))
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.dfs(0,cost), self.dfs(1, cost))

        