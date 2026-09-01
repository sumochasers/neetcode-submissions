class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1,2,3,4,5
        k = 2

        54321

        

        4,5,1,2,3
        """
        k = k % len(nums)
        def reverse(i, j):

            while i < j :
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        reverse(0, len(nums) - 1)
        reverse(0, k-1)
        reverse(k, len(nums) - 1)            
        
