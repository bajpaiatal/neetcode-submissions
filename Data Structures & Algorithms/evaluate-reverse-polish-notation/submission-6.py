class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for s in tokens:
            if s in ['+', '-', '*', '/']:
                if len(st)<2:
                    return -1
                val1, val2 = st[-1], st[-2]
                st.pop()
                st.pop()
                match s:
                    case '+':
                        st.append(val1+val2)
                    case '-':
                        st.append(val2-val1)
                    case '*':
                        st.append(val2*val1)
                    case '/':
                        st.append(int(val2/val1))
            else:
                st.append(int(s))
            # print(st)
        if not st:
            return -1
        else:
            return st[0]