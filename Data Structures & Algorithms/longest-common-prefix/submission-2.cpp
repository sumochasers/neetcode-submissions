class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        bool is_unmatched = false;
        int i = 0;
        while (i < strs[0].size()){
            for (const auto str : strs){
                if (strs[0][i] != str[i]){
                    string res (strs[0].begin(), strs[0].begin()+i);
                    return res;
                }
            }
            i++;
        }
        return strs[0];
       
        
    }
};