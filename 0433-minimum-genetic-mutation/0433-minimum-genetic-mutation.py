class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        bank = set(bank)
        
        queue = deque()
        
        queue.append(start)
        
        visited = set()
        
        level = 0
        
        while len(queue) > 0:
            
            n = len(queue)
            
            for i in range(n):
                
                x = queue.popleft()
                visited.add(x)
                
                if x == end:
                    return level
                
                x = list(x)
                
                for pos in range(len(x)):
                    
                    for char in ["A", "G", "C", "T"]:
                        
                        mut = copy.deepcopy(x)
                        mut[pos] = char
                        string = "".join(mut)
                        
                        if string not in visited and string in bank:
                            queue.append(string)
            level += 1
            
        return -1
                        
                    