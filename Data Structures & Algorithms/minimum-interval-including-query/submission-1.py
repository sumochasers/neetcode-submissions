class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        res = []
        for q in queries :
            minLength = float('inf')
            for left,right in intervals :
                if (left <= q <= right) :
                    minLength = min(minLength, (right - left + 1))
            # if minLength == float('inf') :
            #     minLength = -1
            # res.append(minLength)
            res.append(-1 if minLength == float('inf') else minLength)
        return res
