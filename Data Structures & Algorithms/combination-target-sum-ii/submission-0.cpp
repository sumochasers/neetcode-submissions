class Solution {
public:
    vector<vector<int>> res;
    void dfs_backtrack(vector<int>& candidates,int target, int sum, int index, vector<int> &list){
        
        if ( index >= candidates.size() || sum >= target){
            if (target == sum){
                res.push_back(list);
            }
            return;
        }
        list.push_back(candidates[index]);
        dfs_backtrack(candidates, target, sum+candidates[index],index+1,list);
        list.pop_back();
        while (index+1 < candidates.size() && candidates[index] == candidates[index+1]){
            index ++;
        }
        dfs_backtrack(candidates, target, sum,index+1,list);

    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {

        vector<int> list;
        sort(candidates.begin(), candidates.end());
        dfs_backtrack(candidates,target,0,0,list);
        return res;
        
    }
};
