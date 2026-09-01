class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:

        if len(self.min_heap)== 0 or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else :
            heapq.heappush(self.max_heap, -num)
        
        if len(self.min_heap) > len(self.max_heap) + 1 :
            heapq.heappush(self.max_heap, -self.min_heap[0])
            heapq.heappop(self.min_heap)
        elif len(self.max_heap) > len(self.min_heap) + 1 :
            heapq.heappush(self.min_heap, -self.max_heap[0])
            heapq.heappop(self.max_heap)

        print(self.min_heap)
        print(self.max_heap)

    def findMedian(self) -> float:
        
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else :
            return ((self.min_heap[0] + (-self.max_heap[0]))/2)       
        