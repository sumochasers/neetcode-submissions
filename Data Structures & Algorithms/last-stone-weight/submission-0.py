class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1 :
            
            largest = heapq.heappop(stones);
            secondlargest = heapq.heappop(stones);

            if abs(largest) > abs(secondlargest) :
                heapq.heappush(stones, largest-secondlargest)

        stones.append(0)
        return abs(stones[0])
        

        