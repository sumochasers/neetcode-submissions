class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        data_set = set()
        for num in nums :
            data_set.add(num)

        print(data_set)    
        
        max_len = 0
        for data in  data_set :

            length = 1
            while (data+length) in data_set :
                length +=1
            
            max_len = max(max_len,length)

        print(max_len)
        return max_len         



        