class Solution:
    
    def post_order_dfs(self, node_idx, adjList, visited, cycle, res_stack):
        
        if node_idx in cycle :
            return False
        
        if node_idx in visited :
            return True
        
        cycle.add(node_idx)

        for idx in adjList[node_idx] :
            if not self.post_order_dfs(idx, adjList, visited, cycle, res_stack):
                return False
        
        cycle.remove(node_idx)
        visited.add(node_idx)
        res_stack.append(node_idx)
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            source, destination = edge
            adjList[source].append(destination)
        
        cycle = set()
        visited = set()
        res_stack = []
        for node_idx in range(numCourses):
            if not self.post_order_dfs(node_idx, adjList, visited, cycle, res_stack) :
                return []
        
        return res_stack