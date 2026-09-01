class Solution {
public:
    vector<vector<int>> res;

    void dfs(const vector<int>& nums, vector<int>& sublist, int index){
        
        
        if (index >= nums.size()){
            
            vector<int> copy = sublist;
            res.push_back(copy);
            return;
        }
        
        sublist.push_back(nums[index]);
        dfs(nums,sublist,index+1);
        sublist.pop_back();
        dfs(nums,sublist,index+1);

        


    }
    
    vector<vector<int>> subsets(vector<int>& nums) {

        vector<int> sublist; 
        dfs(nums,sublist,0);
        return res;
        
    }
};
