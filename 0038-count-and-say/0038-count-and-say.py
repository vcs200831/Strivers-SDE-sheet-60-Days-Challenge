class Solution:
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return("1")
        a=self.countAndSay(n-1)
        i=0
        s=""
        while(i<len(a)):
            ch=a[i]
            ns=0
            while(i<len(a) and a[i]==ch):
                ns+=1
                i+=1
            s+=str(ns)
            s+=ch
        return(s)