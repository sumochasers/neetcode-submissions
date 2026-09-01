class Solution:
    def jump(self, nums: List[int]) -> int:

        def dfs(i) :
            if i >= len(nums) - 1:
                return 1
            if nums[i] == 0 :
                return 0    

            min_count = 1e9
            
            for j in range(1,nums[i]+1):
               count = dfs(i+j)
               if count > 0 :
                  min_count = min(min_count,count)  
            
            return 1+min_count if min_count > 0 else 0

        return dfs(0)-1


        