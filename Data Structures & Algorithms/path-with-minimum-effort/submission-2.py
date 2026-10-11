class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        min_heap = []
        heapq.heappush(min_heap, [0,[0,0]])
        visited = set()
        directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
        
        while min_heap :
            effort, pos = heapq.heappop(min_heap)
            r, c = pos
            if (r, c) in visited:
                continue
            if (r,c) == (len(heights) - 1, len(heights[0]) -1 ):
                return effort 
            visited.add((r, c))
            
            for dr, dc in directions :
                nr = r + dr
                nc = c + dc
                
                if nr < 0 or nr >= len(heights) or nc < 0 or nc >= len(heights[0]) or (nr, nc) in visited :
                    continue
                
                dist = abs(heights[r][c] - heights[nr][nc])
                newE = max(dist, effort)
                heapq.heappush(min_heap, [newE, [nr,nc]])
            
        return -1
                
