class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Build adjList
        adjList = defaultdict(list)
        N = len(points)
        for i in range(N):
            for j in range(i + 1, N):
                distance = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                adjList[i].append([distance, j])
                adjList[j].append([distance, i])

        res = 0 
        visit = set()
        minH = [[0,0]]

        while len(visit) < N :
            cost, i = heapq.heappop(minH)
            if i in visit :
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adjList[i] :
                if nei not in visit :
                    heapq.heappush(minH, [neiCost, nei])
        return res
