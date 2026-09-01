class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramBucket = {}
        for val in strs :
            sortedVal = "".join(sorted(val))
            if sortedVal in anagramBucket :
                anagramBucket[sortedVal].append(val)
            else :
                anagramBucket[sortedVal] = [val]

        grouped_list = []
        for list in anagramBucket.values():
            grouped_list.append(list)
        return grouped_list  

        