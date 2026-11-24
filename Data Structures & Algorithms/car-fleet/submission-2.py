class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = list(zip(position, speed))
        positions.sort(reverse=True)
        # print(positions)
        st = []
        st.append(positions[0])
        for i in range(1, len(positions)):
            if (target-st[-1][0]) / st[-1][1] >= (target-positions[i][0]) / positions[i][1]:
                continue
            else:
                st.append(positions[i])
            # print(st)
        return len(st)