class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            queue = deque()
            queue.append(beginWord)
            visited = set()
            s = set(wordList)
            ans = 1
            while len(queue) > 0:
                
                n = len(queue)
                
                for i in range(n):
                    
                    x = queue.popleft()
                    
                    if x in visited:
                        continue
                        
                    visited.add(x)
                    
                    if x == endWord:
                        return ans
                    
                    p = list(x)
                    
                    for pos in range(len(endWord)):
                        
                        for alph in range(26):
                        
                            buff = p[pos]
                            p[pos] = chr(ord('a') + alph)
                            
                            g = "".join(p)
                            p[pos] = buff
                            
                            if g not in visited and g in s:
                                queue.append(g)
            
                ans += 1
            
            return 0