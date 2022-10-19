class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = Counter(words)
        
        return [word for word in sorted(d.keys() , key = lambda x : (-d[x], x))[:k]]
    