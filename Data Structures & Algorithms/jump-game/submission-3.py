class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i : int) -> bool :
            
            if i >= len(nums) - 1 :
                return True
            
            if i in cache :
                return cache[i]
            
            for j in range(1, nums[i] + 1):
                if dfs(i + j) :
                    cache[i] = True
                    return True
            
            cache[i] = False
            return False
        
        return dfs(0)

        