class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        res = []
        for q in queries :
            minLength = float('inf')
            for interval in intervals :
                if (interval[0] <= q <= interval[1]) :
                    minLength = min(minLength, (interval[1] - interval[0] + 1))
            if minLength == float('inf') :
                minLength = -1
            res.append(minLength)
        return res
