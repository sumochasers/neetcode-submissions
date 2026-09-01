class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #must have only one duplicate
        res = 0
        for num in nums :
            res = num ^ res
        return res 
        