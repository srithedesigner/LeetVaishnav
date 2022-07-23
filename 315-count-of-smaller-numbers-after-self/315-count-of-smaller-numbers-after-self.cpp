class Solution {
public:
    
    //unordered_map<int, int> ind;
    vector<int> answer;
    
    
    void modm(vector<pair<int,int>>& nums, int s, int m, int e)
    {
        int n1 = m-s+1;
        int n2 = e-m;
        
        vector<pair<int,int>> v1;
        vector<pair<int,int>> v2;
        
        
        for(int i = 0; i<n1; v1.push_back(nums[s+i]), i++);
        for(int i = 0; i<n2;  v2.push_back(nums[m+i+1]),i++);
        
        
        int i = 0;
        int j = 0;
        int k = s;
        int left = 0;
        while(i < n1 && j<n2)
        {
            if(v1[i].first <= v2[j].first)
            {
            
                answer[v1[i].second]+=left;
                nums[k++] = v1[i++];
                
            }
            else
            {
                nums[k++] = v2[j++];
                left++;
            }
        }
        
        while (i < n1) {
            nums[k] = v1[i];
            
            answer[v1[i].second]+= left;
            i++;
            k++;
          }
        
        while (j < n2) {
            nums[k] = v2[j];
            
            j++;
            k++;
          }
        
        
            
        
        
    }
    
    void merge(vector<pair<int,int>>& nums, int s, int e)
    {
        if(s<e)
        {
            int m = s + e;
            m = m/2;
            
            merge(nums, s,m);
            merge(nums, m+1, e);
            
            modm(nums, s,m,e);
        }
    }
    
    
    vector<int> countSmaller(vector<int>& nums) {
        
        vector<pair<int,int>> ns;
        
        for(int i = 0; i< nums.size(); i++)
        {
            ns.emplace_back(nums[i], i);
        }
        
        int n = nums.size();
        
        answer = vector<int>(n, 0);
        
        merge(ns,0,n-1);
        
        return answer;
        
        
        
          
    }
};