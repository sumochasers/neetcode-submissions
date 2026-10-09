class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        dist = []
        for i,num in enumerate(arr) :
           dist.append(abs(x - num))
        print(dist)
        
        left = 0 
        right = len(arr) - 1

        while (right - left + 1) != k :
            if dist[left] > dist[right]:
                left += 1
            else :
                right -= 1
        
        return arr[left : right + 1]
        
        # dist.sort(key=lambda x : (x[0],x[1]))
        # res = []
        # for i in range(k):
        #     res.append(arr[dist[i][1]])
        
        # return sorted(res)

        