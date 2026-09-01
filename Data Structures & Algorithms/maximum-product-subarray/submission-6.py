class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # maxP = minP = res = nums[0]
        # for num in nums[1:] :
        #     candidates = (num, maxP * num, minP * num)
        #     maxP = max(candidates)
        #     minP = min(candidates)
        #     res = max(maxP, res)
        # return res

        maxP = minP = 1
        res = nums[0]
        for num in nums :
            candidates = (num, maxP * num, minP * num)
            maxP = max(candidates)
            minP = min(candidates)
            res = max(maxP, res)
        return res
        