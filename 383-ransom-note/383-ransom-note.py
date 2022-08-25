class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransome = sorted(list(ransomNote))
        magazine = sorted(list(magazine))
        
        for char in magazine:
            if ransome and char == ransome[0]:
                ransome.pop(0)
            
        if ransome:
            return False
        else:
            return True
        