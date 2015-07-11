from collections import deque


class Stack:
    # initialize your data structure here.

    def __init__(self):
        self.queue = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.queue == None:
            self.queue = deque([x])
        else:
            self.queue = deque([x, self.queue])

    # @return nothing
    def pop(self):
        if self.queue != None:
            self.queue.popleft()
            try:
                self.queue = self.queue.popleft()
            except:
                self.queue = None

    # @return an integer
    def top(self):
        return self.queue[0]

    # @return an boolean
    def empty(self):
        return self.queue == None
