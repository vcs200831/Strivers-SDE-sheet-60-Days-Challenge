class Solution:
    
    def fib(self, n: int) -> int:
        if(n in {1,0}):
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        