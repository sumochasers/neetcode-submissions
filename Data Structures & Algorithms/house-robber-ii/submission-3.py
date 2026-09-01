class Solution:
    def dfs(self, i, nums, cache, picked_first):
        if i == (len(nums) - 1) and  picked_first :
            return 0
        if i >= len(nums) :
            return 0
        if cache[i] != -1 :
            return cache[i]    
        
        cache[i] = max( nums[i] + self.dfs(i+2, nums, cache, picked_first), self.dfs(i+1, nums, cache, picked_first))

        return cache[i]


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        cache1 = [-1] * (len(nums))
        cache2 = [-1] * (len(nums))
        return max(self.dfs(0, nums, cache1, True),self.dfs(1, nums, cache2, False))
        