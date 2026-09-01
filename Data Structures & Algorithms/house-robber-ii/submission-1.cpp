class Solution {
public:
    vector<int> cache;
    int dfs(int index, bool flag, vector<int>& nums){
        
       
        if( index >= nums.size() || (flag && index == nums.size()-1)){
            return 0;
        }
        if (cache[index] != -1){
            return cache[index];
        }
        
        cache[index] = max(nums[index] + dfs(index+2,flag,nums), dfs(index+1,flag,nums));
        return cache[index];

    }

    int rob(vector<int>& nums) {
        
        if (nums.size() == 1) return nums[0];
        cache.resize(nums.size(),-1);
        int res1 = dfs(0,true,nums);
        
        for (auto &num : cache ){
            num = -1;
        }

        int res2 = dfs(1,false,nums);
        return max(res1,res2);
    }
};
