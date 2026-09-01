class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(start,end) :
            
            if start > end :
                return -1

            mid =   start + (end - start) // 2 

            if nums[mid] > target :
                return binary_search(start,mid-1)
            elif nums[mid] < target :
                return binary_search(mid+1,end)  
            else :
                return mid
        
        return  binary_search(0, len(nums)-1)           
                    


        