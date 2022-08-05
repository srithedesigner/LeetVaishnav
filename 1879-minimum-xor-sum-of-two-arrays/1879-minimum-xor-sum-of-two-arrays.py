class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        
        @lru_cache(None)
        def recursion(index, bitmask):
            
            
            
            if index >= n:
                return 0
            
            ans = float('inf')
            
            for i in range(n):
                
                if not (bitmask & (1 << i)):
                    
                    ans = min(ans, (nums1[index] ^ nums2[i]) + recursion(index+1, (bitmask | (1 << i))))
            
            return ans
        
        
        return recursion(0, 0)