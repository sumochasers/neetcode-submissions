class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0 
        n = len(intervals)
        START = 0
        END = 1
        res = []
        # [1,2]   [3,4]
        while i < n and intervals[i][END] < newInterval[START] :
            res.append(intervals[i])
            i += 1
        # merge - intervals [1,3]  new - [2,4] 
        # Prepend - intervals [2,4]  new - [0, 1]
        while i < n and intervals[i][START] <= newInterval[END] :
            newInterval[START] = min(intervals[i][START], newInterval[START])
            newInterval[END] = max(intervals[i][END], newInterval[END])
            i += 1
        res.append(newInterval)

        while i < n :
            res.append(intervals[i])
            i += 1
        
        return res

        