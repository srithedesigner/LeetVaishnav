class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        
        int diff = INT_MAX;
        int ans = 0;
        int n = nums.size();
        for(int i = 0; i<n; i++)
        {
            
            int left = 0;
            int right = n-1;
            
            while(left < right)
            {
                if(left == i)
                {
                    left += 1;
                    continue;
                }
                if(right == i)
                {
                    right -= 1;
                    continue;
                }
                
                int curr = nums[left] + nums[right] + nums[i];
                
                if(curr == target)
                    return target;
                
                if (abs(target - curr) < diff)
                {
                    diff = abs(target - curr);
                    ans = curr;
                }
                
                if(curr < target)
                    left ++;
                else
                    right --;
            }
        }
        
        return ans;
    }
};