class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            c_sum = max(num, num + c_sum)
            max_sum = max(max_sum, c_sum)
        
        return max_sum
     
        