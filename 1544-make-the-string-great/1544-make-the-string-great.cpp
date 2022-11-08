class Solution {
public:
    
    bool areBad(char a, char b)
    {
        if (abs(a - b) == 32)
            return true;
        return false;
    }
    
    string makeGood(string s) {
        
        stack<char> stack;
        
        int i = 0;
        
        while(i < s.size())
        {
            while(i < s.size() && stack.size() > 0 and areBad(s[i], stack.top()))
            {
                stack.pop();
                i++;
            }
            
            if(i < s.size())
                stack.push(s[i]);
            i++;
            
        }
        
        cout<<'a' - 'A';
        
        string ans = "";
        
        while(!stack.empty())
        {
            ans += stack.top();
            stack.pop();
        }
        
        reverse(ans.begin(), ans.end());
        return ans;
        
    }
};