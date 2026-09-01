class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            if i == n:
                return 0
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            LIS = dfs(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            memo[i][j + 1] = LIS
            return LIS
        
        return dfs(0, -1)
        
        
        # LIS = [1] * len(nums)

        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j] :
        #             LIS[i] = max(LIS[i], 1 + LIS[j])
        # return max(LIS)
        