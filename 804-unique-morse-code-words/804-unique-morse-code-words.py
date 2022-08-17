class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        maps = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        answer = set()
        
        for word in words:
            
            temp = ''
            
            for ch in word:
                
                mappedChar = ord(ch) - ord('a')
                
                temp += maps[mappedChar]
                
            answer.add(temp)
            
        return len(answer)