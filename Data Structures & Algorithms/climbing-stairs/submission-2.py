class Solution:
    
    def get_stairs(self, i, n):
        if i >= n-1:
            return i == n-1
        
        total = self.get_stairs(i+1, n) + self.get_stairs(i+2, n)

        return total
    
    def climbStairs(self, n: int) -> int:
        return self.get_stairs(0,n) + self.get_stairs(1,n)
        