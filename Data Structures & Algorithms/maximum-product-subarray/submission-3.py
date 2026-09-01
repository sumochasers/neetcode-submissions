class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # maxProduct = float("-inf")
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(i,len(nums)):
        #         product = product * nums[j]
        #         maxProduct = max(maxProduct, product)
        
        # return maxProduct
        maxP = 1
        minP = 1
        res = nums[0]
        for num in nums :
            curMax = maxP * num
            maxP = max(num, curMax, minP * num)
            minP = min(num, curMax, minP * num)
            res = max(res, maxP)
        return res