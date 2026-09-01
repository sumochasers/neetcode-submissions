'''

[1,3][1,5][6,7]

start = 1
end 5 

start = 6 
end = 7


'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []

        intervals.sort(key = lambda x : x[0] )
        
        start,end = intervals[0]
       
        
        for i in range(1,len(intervals)) :
            c_start, c_end = intervals[i]
            
            if c_start >= start and c_start <= end :
                
                end = c_end if c_end > end else end
            
            else :
                
                res.append([start,end])
                start = c_start
                end = c_end

        res.append([start,end])    
        return res              
        

        