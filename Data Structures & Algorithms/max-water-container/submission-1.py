class Solution:
    '''
    1 3 7
    '''
    
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        maxVolume = float('-inf')
        while l < r :
            height  = min(heights[l], heights[r])
            length = r - l
            volume = length * height
            maxVolume = max(maxVolume, volume)
            if heights[l] < heights[r] :
                l += 1
            else :
                r -= 1
        
        return maxVolume
        