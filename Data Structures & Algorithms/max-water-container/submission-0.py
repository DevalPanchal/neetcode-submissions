class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            # calculate area
            area = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, area)

            # if left height is smaller than right move left pointer
            if heights[left] < heights[right]:
                left += 1
            # otherwise move right pointer
            else:
                right -= 1

        return maxArea