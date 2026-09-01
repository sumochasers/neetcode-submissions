class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramBucket = {}
        for val in strs :
            sortedVal = "".join(sorted(val))
            if sortedVal in anagramBucket :
                anagramBucket[sortedVal].append(val)
            else :
                anagramBucket[sortedVal] = [val]
        
        return list(anagramBucket.values())        

        