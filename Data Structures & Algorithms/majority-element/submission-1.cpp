class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        // Space efficient
        // sort(nums.begin(), nums.end());
        // return nums[nums.size()/2] ;

        // Time efficeint
        unordered_map<int, int> freq;
        int max_freq = 0 ;
        int result = 0 ;
        for (const auto &num : nums){
            freq[num]++;
            if (freq[num] > max_freq){
                result = num;
                max_freq = freq[num]; 
            }
        }
        return result;
        
    }
};