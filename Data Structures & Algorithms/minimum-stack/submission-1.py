class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = float('inf')

    def push(self, val: int) -> None:
        if val < self.minval:
            self.minval = val

        self.stack.append((val, self.minval))
        
    def pop(self) -> None:
        val, minval = self.stack[-1]
        self.stack.pop()
        if val == minval:
            if self.stack: 
                self.minval = self.stack[-1][-1]
            else:
                self.minval = float('inf')


    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Retrieve min element => min element must be on top => maintain monotonically decreasing stack
        return self.stack[-1][-1]
