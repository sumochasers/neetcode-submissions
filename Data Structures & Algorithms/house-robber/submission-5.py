class Solution:
    def dfs(self, i , money, cache):
        if i >= len(money) :
            return 0
        if i in cache :
            return cache[i]

        cache[i] = max( money[i] + self.dfs(i + 2, money, cache), self.dfs(i + 1, money, cache))
        return cache[i]
    
    def rob(self, nums: List[int]) -> int:
        cache = {}
        return self.dfs(0, nums, cache)