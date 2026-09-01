class Solution:
    '''
    target - 4 
    index + nums[index] >= 
    3 + 1 >= 4
    target = 3
    '''
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for index in range(len(nums) - 2, -1, -1 ):
            if index + nums[index] >= goal :
                goal = index
        return goal == 0 