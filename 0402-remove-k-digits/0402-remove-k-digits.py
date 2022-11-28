class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        nums = list(num)
        
        stack = deque()
        
        if k >= len(nums):
            return "0"
        
        for i in nums:
            
            while k > 0 and len(stack) > 0 and stack[-1] > i:
                stack.pop()
                k-=1
            
            stack.append(i)
        
        while k:
            k-=1
            stack.pop()
        
        x = "".join(stack).lstrip("0")
        
        if x == "":
            x = "0"
            
        return x
        
        