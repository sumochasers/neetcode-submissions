class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1 :
            return [0]

        
        adj : dict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u) 
        
        indegree : dict[int, int] = {}
        q = deque()
        
        for v, adjL in adj.items() :
            indegree[v]  = len(adjL)
            if len(adjL) == 1 :
                q.append(v)
        
        remaining = n

        while remaining > 2 :
            remaining -= len(q)
            print(q)
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if  indegree[nei] == 1 :
                        q.append(nei)
                    
        return list(q)