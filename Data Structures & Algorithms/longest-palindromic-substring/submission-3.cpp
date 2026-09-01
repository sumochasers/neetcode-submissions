/*

ababd


*/

class Solution {
public:
    
    bool isPalin(const string& s, int start, int end){
        
        while(start < end){
            if (s[start] != s[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;

    }
    
    string longestPalindrome(string s) {
        
        int left = 0 ; 
        int right = 0 ;
        for (int i = 0 ; i < s.size() ; i++){
            for(int j = s.size()-1 ; j > i ; j--){
                if (isPalin(s,i,j)){
                    std::cout << " i is " << i << " J is " << j << std::endl;
                    if((j-i) > (right - left)){
                        left = i;
                        right = j;
                    }
                }
            }
        }
        return s.substr(left,right-left+1);
    }
};
