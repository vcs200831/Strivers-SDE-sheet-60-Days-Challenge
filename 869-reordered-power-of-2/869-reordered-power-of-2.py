class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = Counter(str(n))
        
        for i in range(30):
            res = str(2 ** i)
            if digits == Counter(res):
                return True
        return False
        
        
        
        
        
#         n1 = sorted(str(n))
    
#         for i in range(30):
#             res = sorted(str(2 ** i))
#             if res == n1:
#                 return True
        
        
#         return False


