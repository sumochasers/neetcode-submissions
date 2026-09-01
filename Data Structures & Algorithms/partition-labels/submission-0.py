class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i,num in enumerate(s):
            lastIndex[num] = i

        result = []
        left = 0 
        right = 0
        for i,num in enumerate(s):
            right = max(lastIndex[num], right)
            if i == right :
                result.append(right-left+1)
                left = right+1
        return result
            

        