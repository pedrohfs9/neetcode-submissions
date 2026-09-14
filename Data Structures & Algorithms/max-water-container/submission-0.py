class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1

        for h in range(0, len(heights)):
            area_atual = (right - left) * min(heights[left], heights[right])
            if area_atual > area:
                area = area_atual
            
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        
        return area
