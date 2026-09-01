class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Brute force
        # res = []
        # for r in range(len(nums)):
        #     if r+k <= len(nums) :
        #         max_val = -9999999
        #         for l in range(r,r+k):
        #             if nums[l] > max_val:
        #                 max_val = nums[l]
        #         res.append(max_val)
        # return res

        res = []
        q = deque()
        l = r = 0

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0] :
                q.popleft()

            if (r + 1) >= k :
                res.append(nums[q[0]]) 
                l += 1
            
            r += 1     
        
        return res


               
                    

        