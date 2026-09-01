class Solution {
public:
    string longestPalindrome(string s) {
        int length = s.size();
        // vector<vector<int>> sub_solutions(length, vector<int>(length, 0));
        // int start_index = -1;
        // int current_longest = -1;
        // for(int i = length-1; i >= 0; i-- ){
        //     for (int j = i; j < length ; j++){
        //         if(s[i] == s[j] && ( j-i+1 <= 3 || sub_solutions[i+1][j-1] == 1)){
        //             sub_solutions[i][j] = 1;
        //             if (j-i+1 > current_longest){
        //                 start_index = i;
        //                 current_longest = j-i+1;
        //             } 
        //         }
        //     }
        // }
        vector<vector<int>> sub_solutions(length, vector<int>(length, 0));
        int start_index = -1;
        int current_longest = -1;
        for(int i = 0; i < length ; i++ ){
            for (int j = i; j > -1 ; j--){
                if(s[i] == s[j] && ( i-j+1 <= 3 || sub_solutions[i-1][j+1] == 1)){
                    sub_solutions[i][j] = 1;
                    if (i-j+1 > current_longest){
                        start_index = j;
                        current_longest = i-j+1;
                    } 
                }
            }
        }
        return s.substr(start_index, current_longest);
    }
};
