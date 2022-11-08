class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = deque()
        
        i = 0
        
        
        def isBad(a, b):
            return abs(ord(a) - ord(b)) == 32
        
        
        while i < len(s):
            
            while i < len(s) and len(stack) > 0 and isBad(s[i], stack[-1]):
                stack.pop()
                i+=1
            
            if i < len(s):
                stack.append(s[i])
                i += 1
                
        
        return "".join(list(stack))