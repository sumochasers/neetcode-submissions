class Solution:
    # def dfs(self, i, open, s):
    #     if open < 0 :
    #         return False
    #     if i == len(s):
    #         return open == 0 
    #     if s[i] == '(' :
    #         return self.dfs(i + 1, open + 1, s)
    #     elif s[i] == ')' :
    #         return self.dfs(i + 1, open - 1, s)
    #     else :
    #         return (
    #             self.dfs( i + 1, open + 1, s) or 
    #             self.dfs( i + 1, open - 1, s) or 
    #             self.dfs( i + 1, open, s )
    #         )

    def checkValidString(self, s: str) -> bool:

        # return self.dfs(0, 0, s)

        # leftStack = []
        # starStack = []

        # for i, ch in enumerate(s):
        #     if ch == '(' :
        #         leftStack.append(i)
        #     elif ch == '*' :
        #         starStack.append(i)
        #     else :
        #         if not leftStack and not starStack :
        #             return False
        #         if leftStack :
        #             leftStack.pop()
        #         else :
        #             starStack.pop()
        # while leftStack and starStack :
        #     if leftStack.pop() > starStack.pop():
        #         return False
        # return not leftStack

        minLeft, maxLeft = 0, 0 

        for ch in s :
            if ch == '(':
                minLeft += 1
                maxLeft += 1
            elif ch == ')' :
                minLeft -= 1
                maxLeft -= 1
            else :
                minLeft -= 1
                maxLeft += 1
            
            if maxLeft < 0 :
                return False
            if minLeft < 0 :
                minLeft = 0
        
        return minLeft == 0 

        