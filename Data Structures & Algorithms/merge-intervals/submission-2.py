class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair : pair[0])
        res = []
        START = 0
        END = 1
        for interval in intervals :
            if not res or res[-1][END] < interval[START] :
                res.append(interval)
            else :
                res[-1][END] = max(res[-1][END], interval[END])
        return res

        