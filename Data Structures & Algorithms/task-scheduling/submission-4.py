class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        q = deque()
        freq = Counter(tasks)
        max_heap = [-x for x in freq.values()]
        heapq.heapify(max_heap)
        
        cycle = 0
        while q or max_heap :
            
            if not max_heap :
                cycle = q[0][0]
            
            while q and q[0][0] <= cycle :
                cycle, freq = q.popleft()
                heapq.heappush(max_heap, freq)
            
            if max_heap :
                cycle += 1
                cnt = heapq.heappop(max_heap)
                if cnt + 1 < 0 :
                    q.append([cycle + n, cnt + 1])
                    
        return cycle
            
