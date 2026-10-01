class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.minStack or self.minStack[-1][0] > value:
            self.minStack.append([value, 1])
        elif self.minStack[-1][0] == value:
            self.minStack[-1][1] += 1

    def pop(self) -> None:
        value = self.stack.pop()

        if self.minStack and self.minStack[-1][0] == value:
            self.minStack[-1][1] -= 1

            if self.minStack[-1][1] == 0:
                self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()