from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = atlantic = False

        def dfs(r, c, prevVal):
            nonlocal pacific, atlantic
            if r < 0 or c < 0:
                pacific = True
                return
            if r >= ROWS or c >= COLS:
                atlantic = True
                return
            if heights[r][c] > prevVal:
                return

            tmp = heights[r][c]
            heights[r][c] = float('inf')
            for dx, dy in directions:
                dfs(r + dx, c + dy, tmp)
                if pacific and atlantic:
                    break
            heights[r][c] = tmp

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                pacific = False
                atlantic = False
                dfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])
        return res                






        
        
        pacific_cells  = set()
        atlantic_cells = set()

        for col in range(0,len(heights[0])):
            pacific_cells.add((0,col));
            atlantic_cells.add((len(heights)-1,col))

        for row in range(0,len(heights)):
            pacific_cells.add((row,0))
            atlantic_cells.add((row,len(heights[0])-1)) 

        res = list()
        for row in range(0,len(heights)):
            for col in range (0,len(heights[0])):
                
                if (row,col) in   pacific_cells and (row,col) in atlantic_cells :
                    res.append([row,col]) 

                elif bfs(row,col,pacific_cells) and bfs(row,col,atlantic_cells) :
                    res.append([row,col])
                 
        
        print(res)  
        return res          



        