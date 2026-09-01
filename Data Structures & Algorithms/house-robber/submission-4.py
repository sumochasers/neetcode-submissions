class Solution:
    
    def dfs(self, i, nums, cache):
        if i >= len(nums):
            return 0
        if cache[i] != -1 :
            return cache[i]    
        
        cache[i] = nums[i] + self.dfs(i+2, nums, cache)
        cache[i+1] = self.dfs(i+1, nums, cache)

        return max(cache[i], cache[i+1])


    def rob(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums)+1)
        return self.dfs(0, nums, cache)
       
        