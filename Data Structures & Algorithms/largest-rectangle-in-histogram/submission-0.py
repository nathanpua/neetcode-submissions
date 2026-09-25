class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        # add a zero for area calculation at the end
        heights.append(0)

        # Monotonic Increasing Stack
        # Upon seeing a height that is less than top, 
        # pop all with heights less than or equal to it, use last popped idx as the new start idx

        for idx, height in enumerate(heights):
            start = idx
            while stack and height <= stack[-1][-1]:
                start, cur_height = stack.pop()
                area = max(area, cur_height * (idx-start))

            stack.append((start, height))

        return area
                