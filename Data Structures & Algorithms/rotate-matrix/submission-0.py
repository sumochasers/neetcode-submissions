class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix[0])
        rotated = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                rotated[j][N - 1 - i] = matrix[i][j]

        for i in range(N):
            for j in range(N):
                matrix[i][j] = rotated[i][j] 