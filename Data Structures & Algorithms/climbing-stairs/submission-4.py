class Solution:
    
    def getNumberofWays(self, i, n, cache):
   
        if i > n :
            return 0
        if i == n :
            return 1 
        
        if i in cache :
            return cache[i]
        
        cache[i] = self.getNumberofWays(i + 1, n, cache) + self.getNumberofWays(i + 2, n, cache)
        return cache[i]

    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.getNumberofWays(0, n, cache)