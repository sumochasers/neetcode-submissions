class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()

        def backtrack(path, rest):
            if  len(rest) == 0:
                res.add(tuple(path))
                return
            
            for i in range(len(rest)):
                path.append(rest[i])
                backtrack(path, rest[ :i] + rest[i + 1:])
                path.pop()
        
        backtrack([], nums)
        print(res)
        return list(res)
