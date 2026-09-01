class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
        int n = nums.size();
        vector<int> ans(2*n);
        // for (int index = 0 ; index < 2*n ; index++){
        //     int num_index = index % nums.size() ;
        //     ans[index] = nums[num_index];
        // }

        for (int i = 0 ; i < n ; i++){
            ans[i] = nums[i];
            ans[i+n] = nums[i];
        }
        return ans;
    }
};