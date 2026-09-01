class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
        vector<int> ans(2*nums.size());
        for (int index = 0 ; index < 2*nums.size() ; index++){
            int num_index = index % nums.size() ;
            ans[index] = nums[num_index];
        }
        return ans;
    }
};