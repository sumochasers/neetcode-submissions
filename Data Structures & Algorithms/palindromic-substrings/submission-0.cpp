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
        int count = 0;
        for(int i = s.size()-1 ; i >= 0 ; i--){
            for(int j = i ; j < s.size() ; j++){
                if(ispalindrome(i,j,s)){
                    count++;
                }
            }
        }
        return count;

    }
};
