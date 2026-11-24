class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        st = []
        for c in s:
            if c in ('(', '[', '{'):
                st.append(c)
            elif st and ((c==')' and st[-1]=='(') or (c=='}' and st[-1]=='{') or (c==']' and st[-1]=='[')):
                st.pop()
            else:
                return False
            print(st)
        return st==[]