class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        directions = [[0,1],[0, -1], [1,0], [-1, 0]]
        cache = {}
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        def dfs(i, j, prev):

            if i >= ROWS or \
               j >= COLS or \
               i < 0 or \
               j < 0 or \
               matrix[i][j] <= prev :

               return 0
            
            if (i, j) in cache :
                return cache[(i, j)]
            
            max_len = 1
            # for di, dj in directions:
            #     max_len = max(max_len, 1 + dfs(i + di, j + dj, matrix[i][j]))
            max_len = max(max_len, 1 + dfs(i + 1, j, matrix[i][j]))
            max_len = max(max_len, 1 + dfs(i - 1, j, matrix[i][j]))
            max_len = max(max_len, 1 + dfs(i, j + 1, matrix[i][j]))
            max_len = max(max_len, 1 + dfs(i, j - 1, matrix[i][j]))

            cache[(i, j)] = max_len
            return max_len
        
        max_len = 0
        for i in range(ROWS):
            for j in range(COLS):
                max_len = max(max_len, dfs(i, j, -1))
        
        return max_len
