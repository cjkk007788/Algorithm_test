class Solution:
    def maxArea(self, height: list[int]) -> int:

        left = 0
        right = len(height)-1
        area = 0
        while(left !=right):
            left_height = height[left]
            right_height = height[right]

            base = right - left
            area = max(area, base * min(left_height,right_height))

            if(left_height <= right_height):
                left = left+1
            else:
                right = right-1
            
        return area