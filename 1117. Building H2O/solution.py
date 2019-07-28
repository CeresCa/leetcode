from collections import deque


class H2O:
    def __init__(self):
        self.h_queue = deque()
        self.o_queue = deque()

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.h_queue.append(releaseHydrogen)
        self.build()

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:

        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o_queue.append(releaseOxygen)
        self.build()

    def build(self) -> None:
        if len(self.h_queue) >= 2 and len(self.o_queue) >= 1:
            self.h_queue.pop()()
            self.h_queue.pop()()
            self.o_queue.pop()()

