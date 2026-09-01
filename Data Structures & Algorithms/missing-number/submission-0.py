class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #xorr starts as n 
        #because the loop only covers numbers 0 to n-1, 
        #but the full range we want is 0 to n. 
        #So we manually include n at the start.
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr
        