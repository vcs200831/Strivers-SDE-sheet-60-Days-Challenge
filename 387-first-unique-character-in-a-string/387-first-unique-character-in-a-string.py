class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        
        for x in s:
            freq[x] = freq.get(x,0) + 1
            
        for i in s:
            if freq[i] == 1:
                return s.index(i)
            
        return -1
        