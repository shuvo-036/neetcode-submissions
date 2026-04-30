class MinStack:

    def __init__(self):
        self.Stack =[]
        self.MinStack =[]

    def push(self, val: int) -> None:
        self.Stack.append(val)
        if not self.MinStack or val < self.MinStack[-1]:
            self.MinStack.append(val)

    def pop(self) -> None:
        if self.MinStack[-1] == self.Stack[-1]:
            self.MinStack.pop()
        self.Stack.pop()    

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
