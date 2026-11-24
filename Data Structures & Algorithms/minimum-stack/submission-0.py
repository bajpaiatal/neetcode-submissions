class MinStack:

    def __init__(self):
        self.st = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        if val<self.minVal:
            self.st.append(2*val-self.minVal)
            self.minVal = val
        else:
            self.st.append(val)

    def pop(self) -> None:
        if not self.st:
            return
        val = self.st[-1]
        self.st.pop()
        if val<self.minVal:
            self.minVal = 2*self.minVal-val

    def top(self) -> int:
        if not self.st:
            return -1
        elif self.st[-1]<self.minVal:
            return self.minVal
        else:
            return self.st[-1]

    def getMin(self) -> int:
        return self.minVal
