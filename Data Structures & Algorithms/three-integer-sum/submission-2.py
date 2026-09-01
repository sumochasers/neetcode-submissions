class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        array_len = len(nums)

        nums.sort() 
        
        for i in range(array_len) :
            
            for j in range(i+1, array_len):

                for k in range(j+1,array_len):
                    
                    if nums[i]+nums[j]+nums[k] == 0 :
                        tmp = [nums[i],nums[j],nums[k]]
                        res.add(tuple(tmp))
                        break
                        
        
        return [ list(i) for i in res]                


        