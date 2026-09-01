class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0 :
            return res
        
        count = abs(n)
        while count > 0 :
            res = res * x
            count = count - 1
        
        if n > 0 :
            return res
        else :
            return 1 / res

         
            
        