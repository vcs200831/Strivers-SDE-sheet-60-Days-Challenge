from sortedcontainers import SortedList

class TimeMap:
    
    def __init__(self):
        self.h = defaultdict(lambda: SortedList())
        self.defaultvalue = ''.join('z'*100)
        
    # O(M.L.logM) time
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].add((timestamp, value))
        
    # O(N.L.logM) time
    def get(self, key: str, timestamp: int) -> str:
        i = self.h[key].bisect_right((timestamp, self.defaultvalue))
        return self.h[key][i - 1][1] if i > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)