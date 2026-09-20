class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        right = 0
        total_sum = 0
        min_length = float('inf')
        while right < len(nums) :
            
            total_sum += nums[right]
            
            if total_sum >= target :
                min_length = min(min_length, right - left + 1)
            
            while (total_sum - nums[left]) >= target :
                total_sum -= nums[left]
                left += 1
                min_length = min(min_length, right - left + 1)

            right += 1
        
        if min_length != float('inf') :
            return min_length
        else :
            return 0
        

            
