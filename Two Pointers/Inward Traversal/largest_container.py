# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height) - 1
        while left < right:
            x = right - left
            y =  min(height[right],  height[left])
            area = x * y
            max_water = max(max_water, area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                right -= 1
                left += 1 
        return max_water
            
        