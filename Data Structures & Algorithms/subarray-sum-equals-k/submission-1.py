class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #---Brute Force -------#
        # count = 0
        # for i in range(len(nums)):
        #     local_sum = 0
        #     for j in range(i,len(nums)):
        #         local_sum += nums[j]
        #         if local_sum == k :
        #             count += 1
        # return count
        count = 0
        cur_sum = 0
        prefix_sums = {0 : 1}
        for num in nums :
            cur_sum += num 
            diff = cur_sum - k 
            count += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)
        return count 
            