class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        Set = set()
        
        for i in range(len(s) - k + 1):
            Set.add(s[i: i + k])
            
        return len(Set) == 2 ** k
            