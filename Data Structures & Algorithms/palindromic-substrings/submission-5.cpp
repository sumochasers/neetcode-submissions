class Solution {
public:
    bool ispalindrome(int start, int end, string s){
        if (start == end){
            return s[start] == s[end] ;
        } 
        while(start < end){
            if (s[start] != s[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
    int countSubstrings(string s) {
        //brute force
        //int count = 0;
        // for(int i = s.size()-1 ; i >= 0 ; i--){
        //     for(int j = i ; j < s.size() ; j++){
        //         if(ispalindrome(i,j,s)){
        //             count++;
        //         }
        //     }
        // }
        // return count;

        int count = 0;
        vector<vector<int>> sub_solutions(s.size(), vector<int>(s.size(),0));
        for(int i = s.size()-1 ; i >= 0 ; i--){
            for(int j = i ; j < s.size() ; j++){
                if(s[i]==s[j] && (j-i+1 <=3 || sub_solutions[i+1][j-1] ==1)){
                    sub_solutions[i][j] = 1;
                    count++;
                }
            }
        }
        return count;    



    }
};
