class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        sorted_tasks = [[e_time, p_time, i] for i, (e_time, p_time) in enumerate(tasks)]
        
        sorted_tasks.sort(key = lambda x : x[0])

        res = []
        min_heap = []
        i = 0
        time = 0 
        n = len(tasks)
        
        while i < n or min_heap :
        
            while  i < n and sorted_tasks[i][0] <= time :
                task = sorted_tasks[i]
                heapq.heappush(min_heap, (task[1], task[2]))
                i = i + 1
            
            if not min_heap :
                time = sorted_tasks[i][0]
            
            else :
                next_task = heapq.heappop(min_heap)
                res.append(next_task[1])
                time += next_task[0]
        
        return res



            


