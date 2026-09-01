/*

  1 2 3
  1 3 2
  2 1 3
  2 3 1
  3 1 2
  3 2 1

*/

class Solution {
public:
    
    std::vector<std::vector<int>> res;
   
    void dfs(vector<int>& visited, vector<int>&nums){

        if( visited.size() == nums.size()){
            vector<int> temp;
            for (const int &num : visited){
                temp.push_back(num);
            }
            res.push_back(temp);
            return;
        }
        
        for (int i = 0 ; i < nums.size() ; i++){
            if (std::find(visited.begin(),visited.end(),nums[i]) == visited.end()){
                visited.push_back(nums[i]);
                dfs(visited, nums);
                visited.pop_back();
            }
            
        }
       
        


    }
    
    vector<vector<int>> permute(vector<int>& nums) {

        std::vector<int> visited;
        dfs(visited,nums);
        return res;

        
    }
};
