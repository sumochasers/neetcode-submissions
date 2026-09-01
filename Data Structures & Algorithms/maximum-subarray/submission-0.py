class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]
        total_sum = 0 
        i = 0 
        
        while i < len(nums) :
            
            total_sum +=nums[i]
            max_sum  = max(total_sum,max_sum)
            if total_sum < 0 :
                total_sum = 0
            i +=1    
        
        print(max_sum)   
        return max_sum     
               
            
              


        