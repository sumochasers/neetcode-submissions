class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        target = sum(nums) // k
        buckets = [0] * k

        nums.sort(reverse=True)

        def dfs(index):

            if index == len(nums) :
                return True
            
            for i in range(k):
                if buckets[i] + nums[index] > target :
                    continue
                
                buckets[i] += nums[index]
                if dfs(index + 1):
                    return True
                buckets[i] -= nums[index]

                if buckets[i] == 0 :
                    break

            return False
        
        return dfs(0)


