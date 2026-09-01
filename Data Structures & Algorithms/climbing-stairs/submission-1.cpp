class Solution {
public:
    int ways = 0;
    
    void dfs(int sum, int n){
        if (sum > n){
            return;
        }
        if (sum == n){
            ways++;
        }
        dfs(sum+1,n);
        dfs(sum+2,n);
    }

    int climbStairs(int n) {
        dfs(0,n);
        std::cout << ways;
        return ways;
    }
};
