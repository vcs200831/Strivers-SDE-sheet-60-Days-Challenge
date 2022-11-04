class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        def swap(a,b):
            s[a],s[b]=s[b],s[a]
        vowels="aeiouAEIOU"
        l=0
        r=len(s)-1
        while l<r:
            if s[l] in vowels and s[r] in vowels:
                swap(l,r)
                l+=1
                r-=1
            elif s[l] in vowels:
                r-=1
            elif s[r] in vowels:
                l+=1
            else:
                l+=1
                r-=1
        return "".join(s)