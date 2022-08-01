class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        def find_pivot(nums):
            
            low = 0
            high = len(nums) - 1
            
            if nums[low] < nums[high]:
                return 0
            
            while low <= high:
                
                mid = low + (high - low)//2
                
                if mid == 0 and nums[mid] < nums[n-1]:
                    return mid
                
                if mid == 0:
                    low = mid + 1
                    continue
                
                if nums[mid] < nums[mid-1]:
                    return mid
                
                if nums[mid] > nums[mid-1]:
                    
                    if nums[mid] > nums[0]:
                        low = mid + 1
                    else:
                        high = mid - 1
            return low
        
        pivot = find_pivot(nums)
        
        
        def binary_search(nums: List[int], low : int, high: int, target: int) -> int:
            
            while low <= high:
                
                mid = low + (high - low)//2
                
                if nums[mid] == target:
                    return mid
                
                if nums[mid] < target:
                    low = mid + 1
                    
                else:
                    high = mid - 1
                    
            return -1
        
        return max(
            binary_search(nums, 0, pivot-1, target),
            binary_search(nums, pivot, len(nums) - 1, target)
        )
        
        
        
                    
            
            
            