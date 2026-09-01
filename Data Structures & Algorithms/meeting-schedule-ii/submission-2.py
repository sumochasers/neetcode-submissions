"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
[[2,30],[3,15]]
[1,40],[50,60]





'''

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda x : x.start)

        day = 0
        slots = list(intervals)
        while len (slots) != 0:
            
            day +=1
            new_slot = []
            start = slots[0].start
            end = slots[0].end 
            
            for i in range(1,len(slots)):
                c_start, c_end = slots[i].start, slots[i].end
                if c_start >= start and c_start < end :
                    new_slot.append(slots[i])
                else :
                    start, end = c_start, c_end  
            
            slots = list(new_slot)
            print(slots)

        return day    




        


        