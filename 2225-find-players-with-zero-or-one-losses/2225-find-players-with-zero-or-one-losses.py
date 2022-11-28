class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        lost = defaultdict(int)
        s = set()
        
        for win, loss in matches:
            
            lost[loss] += 1
            s.add(loss)
            s.add(win)
        
        ans = [[], []]
        
        for i in s:
            if lost[i] == 0:
                ans[0].append(i)
            if lost[i] == 1:
                ans[1].append(i)
        
        ans[0].sort()
        ans[1].sort()
        
        return ans
    