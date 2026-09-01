class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = float("-inf")
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i])
            minHeight = heights[i]
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                area = (j - i + 1) * minHeight
                maxArea = max(maxArea, area, heights[j])
        return maxArea