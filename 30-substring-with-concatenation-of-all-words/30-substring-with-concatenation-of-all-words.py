class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        hashmap={}
        
        for word in words:
            if word in hashmap:
                hashmap[word] += 1
            else:
                hashmap[word] = 1
                
        answer = []
        
        i = 0
        
        j = (len(words[0]) * len(words)) - 1
        
        while j < len(s):
            
            a = i
            
            b = i + len(words[0]) - 1
            
            t = {}
            
            while b <= j:
                if s[a:b+1] in t:
                    t[s[a:b+1]] += 1
                else:
                    t[s[a:b+1]] = 1
                    
                a = b+1
                b += len(words[0])
                
            if t == hashmap:
                answer.append(i)
                
            i += 1
            j += 1
            
            
            
        return answer
                    
                    
                    
                    
                    
                    
                    
                