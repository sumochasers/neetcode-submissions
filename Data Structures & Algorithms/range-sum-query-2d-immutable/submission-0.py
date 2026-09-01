class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum : list[list[int]] = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.pre_sum[r][c + 1] = matrix[r][c] + self.pre_sum[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = 0
        for row in range(row1, row2 + 1):
            res += self.pre_sum[row][col2 + 1] - self.pre_sum[row][col1]
        
        return res
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)