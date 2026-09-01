'''
    1   2  4  8
    10 11 12 13
    14 20 30 40

    start_row = 0 
    end_row = last_row

    middle row = start + end // 2

    if target in range of this row :
        search the row 
    elif target < middle_row[0]:
        end_row = middle_row - 1
    else 
        start_row = middle_row + 1
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        
        start_row = 0
        end_row = len(matrix) - 1
        
        while start_row <= end_row and end_row <= len(matrix) - 1 :
            
            mid_row_id = (start_row + end_row) // 2
            
            
            mid_row = matrix[mid_row_id]
            if target >= mid_row[0] and target <= mid_row[len(mid_row)-1]:
                for ele in mid_row :
                    if ele == target :
                        return True
                return False        
            
            elif target < mid_row[0]:
                end_row = mid_row_id - 1   
            else :
                start_row = mid_row_id + 1 

        return False        



        