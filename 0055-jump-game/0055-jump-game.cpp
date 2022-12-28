class Solution {
public:
    bool canJump(vector<int>& nums) {
        
        int max_till = 0;
        int current =0;
        while(current<nums.size() && max_till>=current)
        {
            max_till = max(max_till,nums[current]+ current);
            current++;
        }
        
        return max_till>=nums.size()-1;
        
        
    }
};