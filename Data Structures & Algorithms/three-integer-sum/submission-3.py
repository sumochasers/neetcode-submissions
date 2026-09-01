class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = list()
        array_len = len(nums)

        nums.sort() 

        for i,a in enumerate(nums) :
            
            if a > 0 :
                continue
            
            if i > 0 and a == nums[i-1] :
                continue

            l, r = i+1 , array_len -1
            
            while l < r :
                
                threeSum = nums[i] + nums[l] + nums[r] 
                
                if threeSum > 0:
                    r = r - 1

                elif  threeSum < 0 :
                    l = l + 1  

                else :
                    
                    res.append([nums[i],nums[l],nums[r]])
                    r = r - 1
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r :
                        l += 1

        print(res)
        return res                 








        