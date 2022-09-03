class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        self.ans = []
        
        self.dfs(n,k,'',-1)
        
        return self.ans
        
        
        
    def dfs(self,n,k,asf,prev):
            
            
        if n == 0:
                
            self.ans.append(asf)
            return 
            
            
        for i in range(10):
                
            if prev == -1:
                    
                if i == 0:
                    
                    continue
                    
                self.dfs(n-1,k,asf+str(i),i)
                    
            else:
                    
                if abs(i - prev) == k:
                        
                    self.dfs(n-1,k,asf+str(i),i)
                
                    
                