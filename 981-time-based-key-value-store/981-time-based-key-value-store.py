from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        
        self.ds = defaultdict(SortedList)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].add((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        x = self.ds[key].bisect_right((timestamp, '~'))
        
        if x == 0:
            return ""
        
        return self.ds[key][x-1][1]
