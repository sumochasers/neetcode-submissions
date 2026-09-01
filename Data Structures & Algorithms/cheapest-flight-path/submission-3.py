class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # prices = [float('inf') for _ in range(n)]
        # prices[src] = 0
        
        # for i in range(k + 1) :
        #     tmpPrices = prices.copy()

        #     for s, d, p in flights :
        #         if prices[s] == float('inf'):
        #             continue
        #         if prices[s] + p < tmpPrices[d] :
        #             tmpPrices[d] = prices[s] + p
        #     prices = tmpPrices
        
        # return -1 if prices[dst] == float("inf") else prices[dst]

        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])

        q = deque([(0, src, 0)])
        while q:
            cst, node, stops = q.popleft()
            if stops > k :
                continue

            for nei, w in adj[node]:
                nextCost = cst + w
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1