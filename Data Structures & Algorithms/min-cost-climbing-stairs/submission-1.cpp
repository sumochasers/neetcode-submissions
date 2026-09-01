class Solution {
public:
    
    int dfs(int index, vector<int>& cost){
        if (index > cost.size()){
            return 0;
        }
        return cost[index] + std::min(dfs(index+1,cost),dfs(index+2,cost));
    }

    int minCostClimbingStairs(vector<int>& cost) {
        return std::min(dfs(0,cost),dfs(1,cost));
    }
};
