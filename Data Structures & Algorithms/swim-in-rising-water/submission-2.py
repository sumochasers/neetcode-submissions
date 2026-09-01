class Solution:
    
    # def dfs(self, row, col, grid, time, visited):

    #     if row < 0 or col < 0 or row >= len(grid) or col >= len(grid) or visited[row][col]:
    #         return float("inf")
        
    #     if row == len(grid) - 1 and col == len(grid) - 1:
    #         return max(time, grid[row][col])
        
    #     visited[row][col] = True
    #     t = max(time, grid[row][col])

    #     res = min(self.dfs(row + 1, col, grid, t, visited),
    #                self.dfs(row - 1, col, grid, t, visited),
    #                self.dfs(row, col + 1, grid, t, visited),
    #                self.dfs(row, col - 1, grid, t, visited),
    #     )
    #     visited[row][col] = False
    #     return res

    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # visited = [[False for _ in range(len(grid[0]))] for i in range(len(grid))]
        # visited = []
        # for i in range(len(grid)):
        #     row = []
        #     for j in range(len(grid[0])):
        #         row.append(False)
        #     visited.append(row)

        # return self.dfs(0, 0, grid, 0, visited);

        minHeap = [(grid[0][0], 0, 0)]

        visit = set()
        visit.add((0, 0))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while minHeap :
            t, row, col = heapq.heappop(minHeap)
            if row == len(grid) - 1 and col == len(grid[0]) - 1 :
                return t
            for dr, dc in directions :
                nR = row + dr
                nC = col + dc 
                if (nR < 0 or nC < 0 or nR >= len(grid) or
                    nC >= len(grid[0]) or (nR,nC) in visit):
                    continue
                visit.add((nR, nC))
                heapq.heappush(minHeap,(max(t, grid[nR][nC]), nR, nC))





    
        