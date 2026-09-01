class Solution:
    
    # def dfs(self, node, adjList, n, res):
    #     if len(res)  == n + 1 :
    #         return True
    #     if node not in adjList :
    #         return False
    #     temp = list(adjList[node])
    #     for i, v in enumerate(temp):
    #         adjList[node].pop(i)
    #         res.append(v)
    #         if self.dfs(v, adjList, n, res):
    #             return True
    #         adjList[node].insert(i, v)
    #         res.pop()
    #     return False

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #adjList
        # adjList = defaultdict(list)
        # tickets.sort()
        # for src, dst in tickets :
        #     adjList[src].append(dst)

        # n = len(tickets)
        # res = ["JFK"]
        
        # self.dfs("JFK", adjList, n, res)
        # return res
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        dfs('JFK')
        return res[::-1]