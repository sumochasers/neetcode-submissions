class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_dict = {}
        frequency_buckets = [[] for i in range(len(nums)+1)]

        for i in nums :
            frequency_dict[i] = frequency_dict.get(i,0)+1
        #print(frequency_dict)

        for num,count in  frequency_dict.items():
            frequency_buckets[count].append(num)
        
        #print(frequency_buckets)
        res = []
        for freq_list in  reversed (frequency_buckets) :

            for num in freq_list :
                res.append(num)
                if len(res) == k :
                    return res





        