class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0 :
            heapq.heappush(heap, (-a, 'a'))
        if b > 0 :
            heapq.heappush(heap, (-b, 'b'))
        if c > 0 :
            heapq.heappush(heap, (-c, 'c'))
        
        res = []

        while heap :
            
            freq, ch = heapq.heappop(heap)

            if len(res) > 1 and res[-1] == res[-2] == ch :
                if not heap :
                    break
                freq2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                
                freq2 += 1
                if freq2 < 0 :
                    heapq.heappush(heap, (freq2, ch2))
                
                heapq.heappush(heap, (freq, ch))
                
            else :
                res.append(ch)
                freq += 1
                if freq < 0 :
                    heapq.heappush(heap, (freq, ch))
                
        
        return "".join(res)
                
        