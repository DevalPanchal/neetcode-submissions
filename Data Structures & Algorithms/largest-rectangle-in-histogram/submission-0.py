class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                idx = stack.pop()
                height = heights[idx]
                left = stack[-1] + 1 if stack else 0
                width = i - left
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea
        