

'''



Find the connected parts - Store the length
directions - up,down,left and right
Am I allowed to mutate the grid ?
Yes - Mark 
No - store it in list 

 fetchConnetedLength(i,j);
    if i,j in boundarycondition :
        return 0 
    else :
            input_matrix[i][j] = 0
            total = 0 
            for directions in allthedirections 
                total =  1 + fetchConnetedLength(i,j)  

max_len = -1
for coordinate in everycoordinates :
    max_len = max(max_len, fetchConnetedLength(0,0))



'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def get_connected_length(i,j):

            if i < 0 or j< 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            total = 1
            for direction in directions :
                dx,dy = direction
                dx = i + dx
                dy = j + dy
                total +=  get_connected_length(dx,dy)

            return total


        max_len = -1
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                max_len = max(max_len,get_connected_length(i,j))        

        return max_len







        