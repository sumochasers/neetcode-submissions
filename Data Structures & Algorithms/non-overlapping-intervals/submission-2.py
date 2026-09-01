class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key= lambda x : (x[1]))
        prevInterval = intervals[0]
        tobeRemoved = 0 
        for i in range(1,len(intervals)):
            if prevInterval[1] > intervals[i][0] :
                tobeRemoved += 1
            else :
                prevInterval = intervals[i]
        return tobeRemoved


        