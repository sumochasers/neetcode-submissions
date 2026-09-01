class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # res = []
        # for q in queries :
        #     minLength = -1
        #     for left,right in intervals :
        #         if (left <= q <= right) :
        #             length = (right - left  + 1)
        #             if minLength == -1 or length < minLength:
        #                 minLength = length
        #     res.append(minLength)
        # return res

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        intervals.sort(key = lambda x : x[0])
        
        min_heap = []
        i = 0
        res = [-1] * len(queries) 
        for q, pos in sorted_queries :
            while i < len(intervals) and q >= intervals[i][0]:
                heapq.heappush(min_heap, ((intervals[i][1] - intervals[i][0] + 1), intervals[i][1]))
                i += 1
            
            while min_heap and min_heap[0][1] < q :
                heapq.heappop(min_heap)
            
            if min_heap :
                res[pos] = min_heap[0][0] 
        
        return res 
