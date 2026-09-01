class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        
        res = []
        for r in range(len(nums)):
            if r+k <= len(nums) :
                max_val = -9999999
                for l in range(r,r+k):
                    if nums[l] > max_val:
                        max_val = nums[l]
                res.append(max_val)
        return res



               
                    

        