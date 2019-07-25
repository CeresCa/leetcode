class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.stackMin = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        self.stackMin.append(min([x] + self.stackMin[-1:]))

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.stackMin.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.stackMin[-1]
