class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [1, 0]
        graph = defaultdict(list)
        in_degrees = defaultdict(int)
        nodes = set()
        
        for preq in prerequisites :
            u = preq[1]
            v = preq[0]
            graph[u].append(v)
            in_degrees[v] += 1
            nodes.add(u)
            nodes.add(v)

        
        q = deque()
        
        for course in range(numCourses):
            if in_degrees[course] == 0:
                q.append(course)
        
        # for node in nodes:
        #     if in_degrees[node] == 0 :
        #         q.append(node)

        res = [] 
        while q :
            node = q.popleft()
            res.append(node)
            
            for nei in graph[node]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 0 :
                    q.append(nei)
        
        return len(res) ==  numCourses 
            

            

        



        