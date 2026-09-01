class Solution:
    
    def post_order_dfs(self, node_idx, adjList, visited):
        
        if node_idx in visited :
            return False
        
        visited.add(node_idx)

        for idx in adjList[node_idx] :
            if not self.post_order_dfs(idx, adjList, visited):
                return False
        
        visited.remove(node_idx)
        return True
        
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            source, destination = edge
            adjList[source].append(destination)
        
        visited = set()
        for node_idx in range(numCourses):
            if not self.post_order_dfs(node_idx, adjList, visited) :
                return False
        
        return True
        
       

        
