class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        l, h = 0, n-1
        while l<h:
            res = max(res, (h-l)*min(heights[h], heights[l]))
            if heights[l]<heights[h]:
                l += 1
            else:
                h -= 1

        return res