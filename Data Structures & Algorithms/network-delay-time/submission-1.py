class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # adjMap = defaultdict(list)
        # for src, dest, time in times :
        #     adjMap[src-1].append([time, dest-1])
        
        # timeList = [float("+inf") for _ in range(n)]
        # timeList[k-1] = 0

        # minH = [[0,k - 1]]

        # while minH :
        #     time, node = heapq.heappop(minH)

        #     if time > timeList[node]:
        #         continue
            
        #     for neiT, neiN in adjMap[node]:
        #         newTime = time + neiT
        #         if newTime < timeList[neiN] :
        #             timeList[neiN] = newTime
        #             heapq.heappush(minH, [newTime, neiN])

        # res = float("-inf")
        # for time in timeList :
        #     if time == float("inf"):
        #         return -1
        #     res = max(res, time)

        # return res

        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}
        q = deque([(k, 0)])
        dist[k] = 0

        while q:
            node, time = q.popleft()
            
            for nei, w in adj[node]:
                if time + w < dist[nei]:
                    dist[nei] = time + w
                    q.append((nei, time + w))

        res = max(dist.values())
        return res if res < float('inf') else -1
              
            


        