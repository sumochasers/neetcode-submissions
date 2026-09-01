class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq_by_ch = Counter(s)

        heap = []

        for ch, freq in freq_by_ch.items() :
            heapq.heappush(heap, (-freq, ch))
        
        res = []

        prev_ch = None
        while heap :
            if heap[0][1] == prev_ch :
                freq1, ch1 = heapq.heappop(heap)

                if not heap :
                    return ""
                
                freq2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                prev_ch = ch2

                freq2 += 1
                if freq2 < 0 :
                    heapq.heappush(heap, (freq2, ch2))
                
                heapq.heappush(heap, (freq1, ch1))
            
            else :
                freq, ch = heapq.heappop(heap)
                res.append(ch)
                
                freq += 1
                if freq < 0 :
                    heapq.heappush(heap, (freq, ch))
                
                prev_ch = ch 
        
        return "".join(res) 

            

