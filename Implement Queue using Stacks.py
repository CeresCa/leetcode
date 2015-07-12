class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.helper = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        while self.stack != []:
            self.helper.append(self.stack.pop())
        self.stack.append(x)
        while self.helper != []:
            self.stack.append(self.helper.pop())

    # @return nothing
    def pop(self):
        self.stack.pop()

    # @return an integer
    def peek(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return self.stack == []
