#User function Template for python3
import math

class Solution:
    def nthFibonacci(self, n):
        x,y=0,1
        for i in range(2,n+1):
            x,y=y,x+y
        return y%1000000007
        
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends