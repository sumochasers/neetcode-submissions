class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        min_len = float('inf')
        total_sum = 0

        for right in range(len(nums)):
            total_sum += nums[right]
            
            while total_sum >= target :
                min_len = min(min_len, right - left + 1)
                total_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len  
        

            
