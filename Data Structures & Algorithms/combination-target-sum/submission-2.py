class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def backtrack(i: int, path : list[int]):
            
            if sum(path) == target :
                res.append(path.copy())
            
            if sum(path) > target :
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j, path)
                path.pop()
        
        backtrack(0, [])
        return res

            

        