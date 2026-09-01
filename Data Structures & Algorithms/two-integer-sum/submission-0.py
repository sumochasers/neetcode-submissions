class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for i,val in enumerate(nums):

            diff = target - val 

            if diff in indices :
                return [indices[diff],i]

            indices[val] = i

        return []        

