class Solution(object):
    def chk(self,i,j):
        if(i=="(" and j==")" ):
            return True
        elif(i=='{' and j=='}'):
            return True
        elif(i=='[' and j==']'):
            return True
        return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif i ==')' or i== '}' or i== ']':
                if(not stack or not self.chk(stack[len(stack)-1],i)):
                    return False
                else:
                    stack.pop()
        if(not stack):
            return True
        else:
            return False

