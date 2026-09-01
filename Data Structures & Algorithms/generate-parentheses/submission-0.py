'''
1
()
2
()(),(())
3- [1,(1,2),(2,1),(3)]
()()(),(())(),()(()),((()))


'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #brute force
        
        def isvalid(substr):
            open = 0 
            for ch in substr :
                open += 1 if ch =='(' else -1
                if open < 0:
                    return False
            
            return True if open == 0 else False     
        
        res = []
        
        def dfs(s):

            if len(s) == 2 * n :
                if isvalid(s) :
                    res.append(s)
                return

            dfs(s+"(") 
            dfs(s+")")
        
        dfs("")
        return res            
                
