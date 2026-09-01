class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        targetCount = len(nums) // 3
        res = set()
        
        for num in nums :
            freq[num] = freq.get(num, 0) + 1
            if freq[num] >  targetCount :
                res.add(num)
        
        return list(res)
        