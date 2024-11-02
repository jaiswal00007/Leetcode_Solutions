class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s+=" " # used as extra spacing for condition evaluation.
        k=""
        p=""
        n=0
        while(n<len(s)-1):
            if(s[n]!=s[n+1] or s[n]!=p): #to evaluate no three consecutives chr are equal and store only necessary one.
                p=s[n]
                k+=s[n]
            n+=1 

        return k
