class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)
        for i, height in enumerate(heights):
            while stack and height <= heights[stack[-1]]:
                idx = stack.pop()

                lidx = stack[-1] if stack else -1 
                width = i - lidx - 1
                
                area = width * heights[idx]
                max_area = max(max_area,area)

            stack.append(i)

        return max_area
