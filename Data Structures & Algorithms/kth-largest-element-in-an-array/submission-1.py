class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        num = [-1*m for m in nums]
        heapq.heapify(num)
        while k != 0 :
            largest = heapq.heappop(num)
            k = k-1
        return (-1 * largest)    


        