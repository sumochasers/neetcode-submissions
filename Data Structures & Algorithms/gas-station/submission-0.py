class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        NUM_STATIONS = len(gas)
        
        
        def dfs(i, capacity, totalCovered):
            if (capacity + gas[i]) < cost[i] :
                return False
            
            if totalCovered+1 == NUM_STATIONS :
                return True
            else :
                nextStation = (i + 1) % NUM_STATIONS
                return dfs(nextStation, capacity+gas[i]-cost[i], totalCovered+1)
        
        for i in range(len(gas)):
            if dfs(i, 0, 0):
                return i
        return -1


