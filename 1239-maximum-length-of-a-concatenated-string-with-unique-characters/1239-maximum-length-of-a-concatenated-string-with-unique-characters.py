class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def recurse(ind : int, s):
            
            if ind >= len(arr):
                return len(s)
            
            
            for c in arr[ind]:
                if c in s:
                    return recurse(ind + 1, s)
            
            n_s = set()
            for i in s:
                n_s.add(i)
                
            if len(arr[ind]) == len(set(arr[ind])):
                for i in arr[ind]:
                    n_s.add(i)
                return max(recurse(ind + 1, s), recurse(ind + 1, n_s))
            
            return recurse(ind + 1, s)
        
        return recurse(0, set())