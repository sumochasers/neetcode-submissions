class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        
        for ch in s :
            if ch == '{' or ch == '(' or ch =='[' :
                stack.append(ch)
            else :
                
                if len(stack) == 0 :
                    return False 

                last_ch = stack[-1]    
                if ch == '}' and last_ch == '{'  or ch ==')' and last_ch == '(' or ch ==']' and last_ch =='[' :
                    stack.pop()
                else :
                    break    

        return    len(stack) == 0       



        