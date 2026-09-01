class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        indegree = {u : 0 for u in range(numCourses)}

        neibors : dict[int, list[int]] = { u : [] for u in range(numCourses)}
        for u,v in prerequisites :
            indegree[v] += 1
            neibors[u].append(v)
        
        que = deque([u for u in indegree if indegree[u] == 0 ])
        dep_set : dict[int, set[int]] = {u : set() for u in range(numCourses)}

        while que :
            node = que.popleft()
            for nei in neibors[node]:
                indegree[nei] -= 1
                dep_set[nei].add(node)
                if dep_set[node] :
                    dep_set[nei].update(dep_set[node])
                if indegree[nei] == 0 :
                    que.append(nei)
        print(dep_set)
        res = []
        for u,v in queries :
            if u in dep_set[v]:
                res.append(True)                
            else :
                res.append(False)
        
        return res
        """
        1. Why should I do topological ordering?
        """
