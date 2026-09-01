class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        res = []
        for q in queries :
            minLength = -1
            for left,right in intervals :
                if (left <= q <= right) :
                    length = (right - left  + 1)
                    if minLength == -1 or length < minLength:
                        minLength = length
            res.append(minLength)
        return res
