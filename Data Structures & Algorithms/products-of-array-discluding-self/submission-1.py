class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre_fix = [1] * len(nums)
        for i in range(1, len(nums)):
            pre_fix[i] = pre_fix[i - 1] * nums[i - 1]
        
        post_fix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            post_fix[i] = post_fix[i + 1] * nums[i + 1]
        
        res = []
        for i in range(len(nums)):
            res.append(pre_fix[i] * post_fix[i])
        
        return res

