class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # ROWS = len(grid)
        # COLS = len(grid[0])
        # LAND = 2**31 - 1
        # WATER = -1
        # visit = [[False for _ in range(COLS)] for _ in range(ROWS)]
        
        # def dfs(i,j):
        #     if i < 0 or j < 0 or \
        #       i >= len(grid) or j >= len(grid[0]) or \
        #       grid[i][j] == WATER or visit[i][j] :
        #         return LAND
            
        #     if grid[i][j] == 0 :
        #         return 0
        #     visit[i][j] = True
        #     min_distance = 1 + min(
        #         dfs( i+1, j ),
        #         dfs( i-1, j ),
        #         dfs( i, j+1 ),
        #         dfs( i, j-1 )
        #     )
        #     visit[i][j] = False
        #     return min_distance
           
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == LAND:
        #             grid[r][c] = dfs(r, c)

        ROWS, COLS = len(grid), len(grid[0])
        LAND = 2**31 - 1
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r,c = q.popleft()

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == LAND:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))        
    

        