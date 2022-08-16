class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            
            mid = low + (high - low)//2
            
            if mid == 0:
                mid += 1
            
            if 0 < mid < len(arr) -1 and arr[mid-1] < arr[mid] > arr[mid + 1]:
                return mid
            
            
            
            
            if 0 < mid and arr[mid] > arr[mid-1]:
                
                low = mid + 1
            
            else:
                
                high = mid - 1
        
        return low