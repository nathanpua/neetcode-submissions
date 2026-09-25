class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # greedily move the shorter bar inwards
        l, r = 0, len(heights) - 1

        area = 0

        while l < r:
            area = max(area, (r-l) * min(heights[r], heights[l]))

            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1

        return area