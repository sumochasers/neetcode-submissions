class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        last = 0 
        
        for i in range(1, len(nums)) :
            if nums[last] == nums[i] :
                continue
            
            last += 1
            nums[last] = nums[i]
            
        return last + 1