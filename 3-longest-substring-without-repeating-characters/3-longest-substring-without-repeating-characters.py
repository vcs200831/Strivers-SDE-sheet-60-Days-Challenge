class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        
        l = 0 
        
        result = 0
        
        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l+=1
             
            Set.add(s[r])
            
            result = max(result,r-l+1)
            
        return result
            