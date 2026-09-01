class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjMap = defaultdict(list)
        for src, dest, time in times :
            adjMap[src-1].append([time, dest-1])
        
        timeList = [float("+inf") for _ in range(n)]
        timeList[k-1] = 0

        minH = [[0,k - 1]]

        while minH :
            time, node = heapq.heappop(minH)

            if time > timeList[node]:
                continue
            
            for neiT, neiN in adjMap[node]:
                newTime = time + neiT
                if newTime < timeList[neiN] :
                    timeList[neiN] = newTime
                    heapq.heappush(minH, [newTime, neiN])

        res = float("-inf")
        for time in timeList :
            if time == float("inf"):
                return -1
            res = max(res, time)

        return res
              
            


        