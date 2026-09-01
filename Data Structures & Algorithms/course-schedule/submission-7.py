class Solution:
    
    @staticmethod
    def preDfs(nodeIdx, adjList, state):
        
        if state[nodeIdx] == 1 :
            return False
        if state[nodeIdx] == 2 :
            return True
        
        state[nodeIdx] = 1

        for neiIdx in adjList[nodeIdx]:
            if not Solution.preDfs(neiIdx,adjList, state):
                return False
        
        state[nodeIdx] = 2

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        state = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]
        for src,dep in prerequisites :
            adjList[src].append(dep)
        
        for node in range(numCourses): 
            if not Solution.preDfs(node, adjList, state):
                return False

        return True

        