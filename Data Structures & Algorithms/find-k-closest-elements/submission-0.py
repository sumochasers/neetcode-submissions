class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        dist = []
        for i,num in enumerate(arr) :
            dist.append((abs(x - num), i))
        dist.sort(key=lambda x : (x[0],x[1]))
        res = []
        for i in range(k):
            res.append(arr[dist[i][1]])
        return sorted(res)

        