class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost) :
            return -1
        
        current = 0
        startStation = 0

        for i in range(len(gas)):
            current += (gas[i] - cost[i])
            if current < 0 :
                current = 0 
                startStation = i + 1 
        return startStation
        
        # NUM_STATIONS = len(gas)
        # def dfs(i, capacity, totalCovered):
        #     if (capacity + gas[i]) < cost[i] :
        #         return False
            
        #     if totalCovered+1 == NUM_STATIONS :
        #         return True
        #     else :
        #         nextStation = (i + 1) % NUM_STATIONS
        #         return dfs(nextStation, capacity+gas[i]-cost[i], totalCovered+1)
        
        # for i in range(len(gas)):
        #     if dfs(i, 0, 0):
        #         return i
        # return -1


