class Solution:
    def dfs(self, i, target, nums):
        if target == 0 :
            return True
        if target < 0 or i >= len(nums):
            return False
        
        return self.dfs(i + 1, target, nums) or self.dfs(i + 1, target-nums[i], nums)


    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 :
            return False
        return self.dfs(0, sum(nums)//2 , nums)