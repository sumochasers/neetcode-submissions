from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(row,col,grid):

            queue = deque()
            queue.append((row,col))
            grid[row][col] = 0
            
            while len(queue) != 0 :
                
                x,y = queue.popleft()
                neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
                for neighbor in neighbors :
                    dx,dy = neighbor
                    
                    dx += x
                    dy += y
                    
                    if dx >= len(grid) or dy >= len(grid[0]) or dx < 0 or dy < 0 or grid[dx][dy] == "0" :
                        continue

                    queue.append((dx,dy))
                    grid[dx][dy] = "0"



        
        
        island_count = 0
        for row in range(0, len(grid)):
            for col in range (0,len(grid[0])):
                if grid[row][col] == "1" :
                    island_count += 1
                    bfs(row,col,grid)
        print(island_count)
        return island_count


        