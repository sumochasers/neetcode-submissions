class Solution:
    
    def dfs(self, i, j, nums):
        if i == len(nums):
            return 0
        count = self.dfs(i + 1, j, nums)
        if j == -1 or nums[i] > nums[j] :
            count = max(count, 1 + self.dfs( i + 1, i, nums))
        return count

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.dfs(0, -1, nums)
        