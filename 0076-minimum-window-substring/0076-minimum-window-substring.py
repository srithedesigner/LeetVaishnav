class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tcounter = Counter(t)
        
        left = 0
        right = 0
        ans = float('inf')
        minstr = ""
        
        cnt = defaultdict(int)
        
        def true():
            
            for i in tcounter:
                if cnt[i] < tcounter[i]:
                    return False
            
            return True
        
        while right < len(s):
            
            while true() and left <= right:
                
                if right - left + 1 < ans:
                    ans = right - left + 1
                    minstr = s[left : right]
                
                cnt[s[left]]-=1
                left += 1
            
            cnt[s[right]] += 1
            right += 1
            
            while true() and left <= right:
                
                if right - left + 1 < ans:
                    ans = right - left + 1
                    minstr = s[left : right]
                
                cnt[s[left]]-=1
                left += 1
            
        
        return minstr
            