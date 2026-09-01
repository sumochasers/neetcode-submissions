'''

    # Check cycles
    # Check all nodes are connected - Max length == number of vertices ? 
    - Build adjacency list 
        for every node run 
        -  Run DFS to find cycle
                # visited set to track vertices


'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) >= n :
            return False
        
        #Build adjacency matrix
        adj_dict = { i : [] for i in range(n)}

        for edge in edges:
            adj_dict[edge[0]].append(edge[1])
            adj_dict[edge[1]].append(edge[0])

        print(adj_dict)
        
        visited_set = set()
        def dfs(v,parent):
            
            if  v in visited_set :
                return False
            
            
            
            visited_set.add(v)
            
            for adjvertex in adj_dict[v] : 
                if parent == adjvertex :
                    continue
                if not dfs(adjvertex,v):
                    return False
            
            return True
        
        is_valid = dfs(0,-1) 
        return True if (is_valid and len(visited_set) == n) else False                 




        