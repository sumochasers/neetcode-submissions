class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)-1):
            end_range = -1
            if i+k >= len(nums) - 1:
                end_range = len(nums)
            else :
                end_range = i+k+1
            for j in range(i+1,end_range):
                if nums[i] == nums[j]:
                    return True
        return False