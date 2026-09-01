class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def bfs (row,col):

            queue = deque()
            queue.append((row,col))

            grid[row][col] == "0"

            while queue :

                #print(queue)
                
                x,y = queue.popleft()

                for direction in directions :
                    dx,dy = direction
                    dx = x+dx
                    dy = y+dy

                    if dx < 0 or dy < 0 or dx >= len(grid)  or dy >= len(grid[0]) or grid[dx][dy] == "0" :
                        continue
                    
                    queue.append((dx,dy))
                    grid[dx][dy] = "0"

        
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" :
                    island_count += 1
                    bfs(i,j)
        
        return island_count  


                        