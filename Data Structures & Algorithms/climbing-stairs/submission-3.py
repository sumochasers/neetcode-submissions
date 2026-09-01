class Solution:
    
    def get_stairs(self, i, n, cache):
        if i >= n:
            return i == n
        if cache[i] != -1 :
            return cache[i]    
        
        cache[i] = self.get_stairs(i+1, n, cache) + self.get_stairs(i+2, n, cache)
        
        return cache[i]
    
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        print(cache)
        self.get_stairs(0, n, cache) 
        return cache[0]
        