class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        for(int i =0; i<9; i++)
        {
            set<int> s;
            s.clear();
            for(int j = 0; j<9; j++)
            {
                if(board[i][j] !='.' && s.count(board[i][j]) !=0)
                    return false;
                s.insert(board[i][j]);
            }
        }
        
        
        for(int i =0; i<9; i++)
        {
            set<int> s;
            s.clear();
            for(int j = 0; j<9; j++)
            {
                if(board[j][i] !='.' && s.count(board[j][i]) !=0)
                    return false;
                s.insert(board[j][i]);
            }
        }
        
        
        vector<int> indx = {0,3,6};
        vector<int> indy = {0,3,6};
        
        for(int i : indx)
        {
            for(int j:indy)
            {
                set<int> s;
                s.clear();
                for(int k = i; k<i+3; k++)
                {
                    for(int l = j; l<j+3; l++)
                    {
                        if(board[k][l] !='.' && s.count(board[k][l]) !=0)
                            return false;
                        s.insert(board[k][l]);
                    }
                }
            }
        }
        
        
        return true;
    }
};