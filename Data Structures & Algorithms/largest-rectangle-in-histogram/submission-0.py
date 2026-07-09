class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            while stack and height <= stack[-1][1]:
                idx, h = stack.pop()
                
                lidx = stack[-1][0] if stack else -1 
                width = i - lidx - 1
                
                area = width * h
                max_area = max(max_area,area)

            stack.append((i,height))

        if stack:
            last = len(heights)
            while stack:
                idx, h = stack.pop()
                lidx = stack[-1][0] if stack else -1
                area = (last - lidx - 1) * h
                max_area = max(max_area,area)

        return max_area
