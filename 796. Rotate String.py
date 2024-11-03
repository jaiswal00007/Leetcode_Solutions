class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)): 
            k=s[1:len(s)] # used list comprehension for storing index 1 to last index of String 's'
            k+=s[0] 
            s=k   #assigning k string to s to rotate string
            if(s==goal): # chk at each iterations
                return True
        return False

