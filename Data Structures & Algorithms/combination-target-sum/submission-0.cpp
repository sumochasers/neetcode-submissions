/*
    nums[1,2,3]  - Target 3
    [1,1,1,1,1]
    [1,2,2]
    [2,3]
                1 
                    -> 1 1
                         1 1 1
                         1 1 2
                       1 2
                         1 2 2
                         1 2 3
                2 
                    2 2 -> 2 2 2
                           2 2 3
                    2 3
                        ->2 3 3
                          2
                  

                
                    
                  
                      
                 


                
*/
class Solution {
public:
    
    vector<vector<int>> res;
    void dfs(const vector<int> &nums, vector<int> list, int index, int sum, int target){
            if (index >= nums.size() || sum >= target ){
                if (sum == target){
                    res.push_back(list);
                }
                return;
            }
            list.push_back(nums[index]);
            dfs(nums,list,index,sum+nums[index],target);
            list.pop_back();
            dfs(nums,list,index+1,sum,target);
    }
    
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> list;
        dfs(nums,list,0,0,target);
        return res;
        
    }
};
