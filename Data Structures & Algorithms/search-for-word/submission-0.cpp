class Solution {
public:
    int ROWS, COLS;
    set<pair<int,int>> visited;

    bool dfs(int x, int y , vector<vector<char>>& board, int index, string word){

        if (index == word.length()){
            return true;
        }

        if ( x < 0 || y < 0 || x >= ROWS || y >= COLS 
                || board[x][y] != word[index] || visited.count({x,y})){
            return false;
        } 

        visited.insert({x,y});
        
        bool res =  dfs(x+1,y,board,index+1,word) || 
                    dfs(x-1,y,board,index+1,word) || 
                    dfs(x,y-1,board,index+1,word) || 
                    dfs(x,y+1,board,index+1,word);
        
        visited.erase({x,y});
        
        //std::cout <<" X , Y " << x << " "<< y  << "Res "<<  res << std::endl;
        return res;


    }
    
    
    
    
    bool exist(vector<vector<char>>& board, string word) {

        ROWS = board.size();
        COLS = board[0].size();
        
        for(int i = 0 ; i < ROWS ; i++){
            for (int j = 0 ; j < COLS ; j++){
                if (dfs(i,j,board,0,word)){
                    return true;
                }
            }
        }
        
        return false;
       
        
    }
};
