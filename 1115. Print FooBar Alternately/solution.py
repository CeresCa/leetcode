import threading


class FooBar:
    """打印之前获取本方法对应的锁，释放对方的锁，barlock先锁住，防止bar先被打印"""

    def __init__(self, n):
        self.n = n
        self.foolock = threading.Lock()
        self.barlock = threading.Lock()
        self.barlock.acquire()

    def foo(self, printFoo: "Callable[[], None]") -> None:
        for i in range(self.n):
            self.foolock.acquire()
            printFoo()
            self.barlock.release()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for i in range(self.n):
            self.barlock.acquire()
            printBar()
            self.foolock.release()
