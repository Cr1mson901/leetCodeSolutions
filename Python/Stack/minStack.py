# Not entirely sure the point in this questiion. Maybe its just to make 2 stacks. Unsure
class MinStack:

    def __init__(self):
        self.min = [float('inf')]
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if self.min[-1] == self.stack.pop():
            del self.min[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]