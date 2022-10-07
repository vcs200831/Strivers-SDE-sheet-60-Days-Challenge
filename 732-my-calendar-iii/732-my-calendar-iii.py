class MyCalendarThree:

    def __init__(self):
        self.times = defaultdict(int)
        
        
        

    def book(self, start: int, end: int) -> int:
        self.times[start] += 1
        self.times[end] -= 1
        result = 0
        current_intersection = 0
        
        for t in sorted(self.times):
            current_intersection += self.times[t]
            result = max(result,current_intersection)
            
        return result
            
        
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)