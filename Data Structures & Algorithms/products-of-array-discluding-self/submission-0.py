class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        res = [1] * len(nums)
        preproducts = [1] * len(nums)
        

        postproducts = [1] * len(nums) 
        

        for i in range(1,len(nums)):
            
            preproducts[i] = nums[i-1] * preproducts[i-1]

        for i in range(len(nums)-2, -1, -1):
            
            postproducts[i] = nums[i+1] * postproducts[i+1]    

        
        for i in range(len(nums)):
            res[i] = preproducts[i] * postproducts[i] 
        
        print(res)
        return res
        #print(postproducts)

        