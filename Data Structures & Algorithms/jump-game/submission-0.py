class Solution:
    def canJump(self, nums: List[int]) -> bool:

        canreach = False
        def dfs(i) :
            nonlocal canreach 
            if  i  >= len(nums) - 1 :
                
                print("yre")
                canreach = True
                return 


            for j in range(1,nums[i]+1):
                dfs(i+j)
            

        dfs(0)
        return canreach            

            