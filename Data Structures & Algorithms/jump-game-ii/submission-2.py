class Solution:
    def jump(self, nums: List[int]) -> int:

        #brute force
        
        def dfs(i) :
            if i >= len(nums) - 1:
                return 0
            
            if nums[i] == 0 :
                return 1e9    

            min_count = 1e9
            
            for j in range(1,nums[i]+1):
                min_count = min(min_count,dfs(i+j))  
            
            return 1+min_count if min_count < 1e9 else 1e9

        return dfs(0)


        