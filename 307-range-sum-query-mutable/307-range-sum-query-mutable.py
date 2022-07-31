class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
        n = len(nums)
        ft = [0]*(n+1)
        
        for i in range(1, len(ft)):
            x = nums[i-1]
            while(i < len(ft)):
                ft[i] += x;
                i += (i&(-i))
                
        self.ft = ft
        
    def sum(self, ind):
        if ind < 1:
            return 0
        
        ans = 0
        while(ind != 0):
            
            ans += self.ft[ind]
            ind -= (ind & (-ind))
        return ans
        
                  
        

    def update(self, index: int, val: int) -> None:
        x = self.nums[index]
        self.nums[index] = val
        val = val - x
        i = index+1
        while(i < len(self.ft)):
            self.ft[i] += val;
            i += (i&(-i))

    def sumRange(self, left: int, right: int) -> int:
        
        suml = self.sum(left)
        sumr = self.sum(right + 1)
        #print(suml, sumr)
        
        return sumr - suml
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)