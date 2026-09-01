class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        parts = []

        def dfs(i):
            if i == len(s):
                res.append(parts.copy())
                return
            
            for j in range(i, len(s)):
                if self.is_palin(s, i, j):
                    parts.append(s[i : j + 1])
                    dfs(j + 1)
                    parts.pop()
        
        dfs(0)
        return res

    def is_palin(self, s, i, j):
        while i < j :
            if s[i] != s[j]:
                return False
            i = i + 1
            j = j - 1
        return True
        