class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        pts_and_distance = []
        for point in points :
            x, y = point
            distance = (x ** 2) + (y ** 2)
            heapq.heappush(pts_and_distance,(distance, point))
        
        res = heapq.nsmallest(k,pts_and_distance)
        result = [x[1] for x in res ]
        print(result)
        return result
        