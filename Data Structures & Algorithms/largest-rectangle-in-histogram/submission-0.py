class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        st = []
        n = len(heights)
        for i, height in enumerate(heights):
            while st and heights[st[-1]] > height:
                h = heights[st[-1]]
                st.pop()
                if not st:
                    w = i
                else:
                    w = i-st[-1]-1
                res = max(res, w*h)
            st.append(i)
        while st:
            h = heights[st[-1]]
            st.pop()
            if not st:
                w = n
            else:
                w = n-st[-1]-1
            res = max(res, w*h)
        return res