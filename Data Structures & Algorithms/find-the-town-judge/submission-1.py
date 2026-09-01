class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        indegree : dict[int, int] = defaultdict(int)
        outdegree : dict[int, int] = defaultdict(int)

        for src, dest in trust :
            outdegree[src] += 1
            indegree[dest] += 1
        
        for node in range(1, n + 1):
            if outdegree[node] == 0 and indegree[node] == n - 1 :
                return node
        return -1
        
        
        