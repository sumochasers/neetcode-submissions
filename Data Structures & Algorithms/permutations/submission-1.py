class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, rest):
            if len(rest) == 0 :
                res.append(path.copy())
                return
            
            for i in range(len(rest)):
                path.append(rest[i])
                dfs(path, rest[:i] + rest[i + 1:])
                path.pop()
            
        dfs([], nums)
        return res
        