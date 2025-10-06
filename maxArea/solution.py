class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            leftValue = height[left]
            rightValue = height[right]
            if leftValue < rightValue:
                current = leftValue * (right - left)
                if maxArea < current:
                    maxArea = current
                left += 1
            else:
                current = rightValue * (right - left)
                if maxArea < current:
                    maxArea = current
                right -= 1
        return maxArea
