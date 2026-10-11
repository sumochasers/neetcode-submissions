class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(candidates)
        def backtrack(i: int, path : list[int], total):
            
            if total == target :
                res.append(path.copy())
            
            if total > target :
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                backtrack(j + 1, path, total + nums[j])
                path.pop()
        
        backtrack(0, [], 0)
        return res