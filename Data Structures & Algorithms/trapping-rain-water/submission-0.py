class Solution:
    def trap(self, heights: List[int]) -> int:
        leftMax, rightMax = 0, 0
        res = 0
        n = len(heights)
        l, h = 0, n-1
        while l<h:
            if heights[l]<heights[h]:
                if heights[l]>leftMax:
                    leftMax = heights[l]
                else:
                    res += leftMax-heights[l]
                l += 1
            else:
                if heights[h]>rightMax:
                    rightMax = heights[h]
                else:
                    res += rightMax-heights[h]
                h -= 1

        return res