class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                res[st[-1][1]] = i-st[-1][1]
                st.pop()
            st.append((temp, i))
        return res
            