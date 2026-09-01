class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        N = len(edges)
        P = [i for i in range(N + 1)]
        R = [1] * (N + 1)

        def find(n):
            if P[n] == n :
                return n
            return find(P[n])
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2 :
                return False
            
            if R[p1] > R[p2]:
                P[p2] = p1
                R[p1] += R[p2]
            else :
                P[p1] = p2
                R[p2] += R[p1]
            
            return True
        
        for n1, n2 in edges :
            if not union(n1, n2):
                return [n1, n2]

        