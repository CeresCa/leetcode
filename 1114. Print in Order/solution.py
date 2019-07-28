from threading import Lock


class Foo:
    """除了first，打印之前都先获取本方法对应锁，打印之后都释放该锁；除了third，打印之后都释放下一个方法的锁"""

    def __init__(self):
        self.second_lock = Lock()
        self.third_lock = Lock()
        self.second_lock.acquire()
        self.third_lock.acquire()

    def first(self, printFirst: "Callable[[], None]") -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_lock.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.second_lock.acquire()
        printSecond()
        self.second_lock.release()
        self.third_lock.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.third_lock.acquire()
        printThird()
        self.third_lock.release()
