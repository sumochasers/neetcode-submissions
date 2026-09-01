class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index_map = {}

        for i,num in enumerate(numbers) :

            remainder = target - num 
            if remainder in index_map :
                return [index_map[remainder], i+1]
            
            index_map[num] = i+1  



        