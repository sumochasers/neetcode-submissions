class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        visited = set()
        def dfs( r : int, c : int):
            
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0 :
                return 1
            if (r,c) in visited :
                return 0
            
            visited.add((r, c))            
            return dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)

        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 :
                    return dfs(i, j)

        