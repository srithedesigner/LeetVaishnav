class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        
        vector<int> ans(queries.size());
        
        int sum = 0;
        
        for(int i : nums)
        {
            if (i%2 == 0)
            {
                sum += i;
            }
        }
        
        for(int q = 0; q < queries.size(); q++)
        {
            int val = queries[q][0];
            int ind = queries[q][1];
            
            if((nums[ind] + val)%2 == 0)
            {
                if(nums[ind]%2 != 0)
                {
                    sum += (nums[ind] + val);
                }
                
                else
                {
                    sum += val;
                }
                
                ans[q] = sum;
                nums[ind] += val;
                continue;
            }
            
            if(nums[ind]%2 == 0)
            {
                sum -= nums[ind];
                
                
            }
            ans[q] = sum;
            nums[ind] += val;
            
            
            
            
        }
        
        
        return ans;
    }
};