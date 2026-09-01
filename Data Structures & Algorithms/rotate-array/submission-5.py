class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        new = nums[-k % len(nums):] + nums[: -k % len(nums)]
        nums[:] = new
        
