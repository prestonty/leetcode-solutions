class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if not self.stack:
            return None
        minimum = self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < minimum:
                minimum = self.stack[i]
        return minimum
