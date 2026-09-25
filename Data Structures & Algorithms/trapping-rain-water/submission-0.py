class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        water = 0

        while l < r:
            if leftmax <= rightmax:
                l += 1
                if height[l] >= leftmax:
                    leftmax = height[l]
                else:
                    water += leftmax - height[l]

            else:
                r -= 1
                if height[r] >= rightmax:
                    rightmax = height[r]
                else:
                    water += rightmax-height[r]
            
        return water