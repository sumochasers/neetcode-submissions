class Solution:
    def sumofSquares(self, n):
        total = 0 
        while n :
            digit = n % 10
            digit = digit ** 2
            total += digit
            n = n // 10
        return total 

        

    def isHappy(self, n: int) -> bool:
        unique = set()

        while n not in unique :
            unique.add(n)
            n = self.sumofSquares(n)
            if n == 1 :
                return True
        
        return False

        
        