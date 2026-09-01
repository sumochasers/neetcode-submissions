class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusted_by : dict[int, set[int]] = {u : set() for u in range(1, n + 1) }
        for u,v in trust :
            trusted_by[v].add(u)
        print(trusted_by)
        
        for node, trusted in trusted_by.items() :
            if len(trusted) == (n - 1) :
                for follower in trusted :
                    if node in trusted_by[follower]:
                        return -1
                return node
        
        return -1
        
        