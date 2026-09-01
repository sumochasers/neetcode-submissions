class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)
        cache = {}
        
        def dfs(i, j):
            if j == n :
                return i == m
            if (i, j) in cache :
                return cache[(i, j)]
            
            match = i < m and ((s[i] == p[j]) or p[j] == '.')

            if (j + 1) < n and p[j + 1] == '*' :
                
                cache[(i, j)] = (match and dfs(i + 1, j)) or dfs(i, j + 2)
                
                return cache[(i, j)]
            if match :
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False

        return dfs(0, 0) 

        