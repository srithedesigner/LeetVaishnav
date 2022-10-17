class Solution {
public:
    
    int fun(int sum){
        
        string s = to_string(sum);
        int small_sum = 0;
        
        cout<<s<<" "<<s.size()<<endl;
        
        if(s.size()==1) {
            return sum;
        }
        
        else{
            for(int i=0;i<s.size();i++){
                small_sum += (s[i] - '0');
            }
            
            return fun(small_sum);
        }
        return 0;
    }
    
    
    
    int addDigits(int num) {
        
       return fun(num);
    }
};
