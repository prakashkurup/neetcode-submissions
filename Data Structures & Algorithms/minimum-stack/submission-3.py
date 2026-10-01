class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.stack or self.stack[-1][0] != val:
            self.stack.append([val, 1])
            if not self.minStack or val < self.minStack[-1][0]:
                self.minStack.append([val, 1])
            elif self.minStack[-1][0] == val:
                self.minStack[-1][1] += 1

            return

        self.stack[-1][1] += 1

    def pop(self) -> None:
        self.stack[-1][1] -= 1
        if self.stack[-1][1] == 0:
            val, _ = self.stack.pop()

            if self.minStack and self.minStack[-1][0] == val:
                self.minStack[-1][1] -= 1
                if self.minStack[-1][1] == 0:
                    self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][0]
