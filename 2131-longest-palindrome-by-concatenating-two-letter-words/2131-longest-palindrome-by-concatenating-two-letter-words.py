class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        c = Counter(words)
        
        ans = 0
        
        oddMiddle = False
        
        for word in c:
            
            rev = word[::-1]
            
            if rev == word:
                
                if c[word]%2 == 1:
                    oddMiddle = True
                
                ans += c[word]//2 * 2
            
            else:
                
                if rev in c:
                    
                    ans += (min(c[word], c[rev]))
                
        
        if oddMiddle:
            ans += 1
        
        return ans * 2
    
            
                
                
                
            