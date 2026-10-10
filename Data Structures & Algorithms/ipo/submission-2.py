class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        capital_profit = [(capital[i],profits[i]) for i in range(len(profits))]
        capital_profit.sort(key = lambda x : x[0])
        i = 0
        max_heap = []
        insufficient = False
        while k and not insufficient:
            while i < len(profits) and capital_profit[i][0] <= w :
                heapq.heappush(max_heap, -capital_profit[i][1])
                i = i + 1
                
            if max_heap :
                max_profit = heapq.heappop(max_heap)
                w = w - max_profit
                k = k - 1
            else :
                insufficient = True
        
        return w

        