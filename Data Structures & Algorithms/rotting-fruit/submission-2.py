'''
    one grid - up,down,left,right - 1 Min
    
    Until queue is empty - iterate every_coordinate - Find next level of rotten bananas
    Every level - 1 min

    Do I have to track rotten coordinates, empty coordinates ?

        Result = (rotten coordinates + empty coordinates) == total
    
    All fruits rotten then Return Time
        sizeof(Total gird) - sizeof(empty Grid)
    Else Return -1
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh_cells = []
        next_queue = deque();
        rotten_list = []
        
        for i in range(0,len(grid)):
            
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1 :
                    fresh_cells.append((i,j))
                if grid[i][j] == 2 :
                    next_queue.append((i,j))
                    #rotten_list.append((i,j))
        
        minutes = 0
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while len(next_queue) != 0 :
            
            minutes += 1
            
            for itr in range(0,len(next_queue)):
                
                x,y = next_queue.popleft()
            
                for direction in directions :
                    dx, dy = direction
                    dx = x + dx
                    dy = y + dy

                    if dx < 0 or dy < 0 or dx >= len(grid) or dy >=len(grid[0]) or grid[dx][dy] == 0 or grid[dx][dy] == 2 :
                        continue
                    else :
                        grid[dx][dy] = 2
                        next_queue.append((dx,dy))
                        rotten_list.append((dx,dy))

        if len(fresh_cells) == len(rotten_list):
            if minutes > 0 :
                return minutes - 1
            else :    
                return 0
        
        else :
            return -1    












        