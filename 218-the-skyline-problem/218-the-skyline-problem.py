from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = defaultdict(list)
        for l, r, h in buildings:
            events[l].append([r, 1, h])
            events[r].append([r, -1, h])
        
        
        l = SortedList([(0, 0)])
        ans = []
        
        for x in sorted(events.keys()):
            for y, t, h in events[x]:
                if t == 1:
                    l.add((h, y))
                else:
                    l.remove((h, y))
            if not ans or ans[-1][1] != l[-1][0]:        
                ans.append([x, l[-1][0]])
        return ans
    