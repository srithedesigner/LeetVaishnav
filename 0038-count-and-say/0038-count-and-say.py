class Solution:
    def countAndSay(self, n: int):
        
        def recursion(s, i):
            
            if i == n:
                return s
            
            ans = []
            for key, group in groupby(s):
                ans.append(str(len(list(group))))
                ans.append(str(key))
            
            return recursion("".join(ans), i+1)
        
        return recursion("1", 1)