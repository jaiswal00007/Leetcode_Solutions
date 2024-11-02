class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s=sentence.split() #converts to list of String seperated with spaces.
        k=s[0][0] # imp for condition evaluation
        j=len(s)-1
        for i in range(len(s)): 
            if(s[i][0]==k): #checking all the iteration for true conditions.
                k=s[i][len(s[i])-1]
            else:
                return False
        if(s[j][len(s[j])-1]==s[0][0]): #at last checking first iteration with last.
            return True
        else:
            return False
