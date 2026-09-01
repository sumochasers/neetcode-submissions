/* 
    Input - int array nums - [index represent house]
    Return - int - maximum amout of money

    1 2 3 4 5 
     
     
   
    

*/
class Solution {
public:
    
    vector<int> cache;
    
    int dfs(vector<int>& nums, int index){
        if (index >= nums.size()){
            return 0;
        }

        if (cache[index] != -1){
            return cache[index];
        }

        cache[index] = max(nums[index]+dfs(nums, index+2), dfs(nums,index+1));
        return cache[index];

    }
    
    int rob(vector<int>& nums) {
        
        cache.resize(nums.size(),-1);
        return dfs(nums,0);
    }
};
