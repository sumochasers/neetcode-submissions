class Solution:
    
    def dfs(self, i, money, containFirst, cache):
        if i >= len(money) or (i == len(money) - 1 and containFirst):
            return 0
        if (i,containFirst)  in cache :
            return cache[(i, containFirst)]

        cache[(i, containFirst)] = max( money[i] + self.dfs(i + 2, money, containFirst, cache),\
                    self.dfs(i + 1, money, containFirst, cache))
        return cache[(i, containFirst)]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}
        return max (self.dfs(0, nums, True, cache), self.dfs(1, nums, False, cache))
        