class Solution {
public:
    
    int xx[4] = {0,0,1,-1};
    int yy[4] = {1,-1, 0,0};
    
    
    bool exist(vector<vector<char>>& board, string word, int n, vector<vector<bool>>& visited, int x, int y)
    {
        if(n >= word.size())
            return true;
        if(x >= board.size() || x <0 || y <0 || y>=board[0].size())
            return false;
        
        if(visited[x][y])
            return false;
        
        if(board[x][y] != word[n])
            return false;
    
        bool ans = false;
        if(word[n] == board[x][y])
        {
           
            
            visited[x][y] = true;
            
            for(int i = 0; i<4; i++)
            {
                int ax = x + xx[i];
                int ay = y + yy[i];
                
                if(exist(board, word, n+1, visited, ax, ay))
                    return true;
                
            }
            
            visited[x][y] = false;
            
            
            
        }
        
        
        
        
        
        return false;
        
    }
    
    
    bool exist(vector<vector<char>>& board, string word) {
        
        
        
        for(int i = 0; i<board.size(); i++)
        {
            for(int j = 0; j<board[0].size(); j++)
            {
                
                vector<vector<bool>> visited((int)board.size(), vector<bool> ((int)board[0].size()));
        
                int n = word.size();

                if(exist(board, word, 0, visited, i,j))
                    return true;
                
               //cout<<endl;
            }
        }
        
        return false;
        
    }
};





/*
A B C E
S F E S
A D E E




            x-1 y
 x y-1       x y     x y+1
            x+1 y
            
            */