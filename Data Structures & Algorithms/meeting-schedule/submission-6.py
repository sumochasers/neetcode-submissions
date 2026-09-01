"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
''' 
(0,30)(5,10)(15,20)
(1,10)(11,20)(23,30)

sort based on start time 

list.sort(key= lambda x : x[0])

'''






class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0 :
            return True

        intervals.sort(key=lambda x : x.start)

        print(intervals[0].start , " " , intervals[0].end)

        start,end = intervals[0].start, intervals[0].end

            
        for i in range(1,len(intervals)):
            c_start, c_end = intervals[i].start, intervals[i].end
            if c_start >= start and c_start < end :
                return False
            start = c_start
            end = c_end

        return True         



