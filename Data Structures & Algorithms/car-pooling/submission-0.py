class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])
        min_heap = []
        cur_pass = 0
        for pass_count, start, end in trips :
            while min_heap and min_heap[0][0] <= start :
                _, count = heapq.heappop(min_heap)
                cur_pass -= count
            
            cur_pass += pass_count
            if cur_pass > capacity :
                return False
            
            heapq.heappush(min_heap, [end, pass_count])
        
        return True
                

        

        
