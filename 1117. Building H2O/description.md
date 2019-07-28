# 题目

> There are two kinds of threads, `oxygen` and `hydrogen`. Your goal is to group these threads to form water molecules. There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given a `releaseHydrogen` and `releaseOxygen` method respectfully, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must be able to immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond *before* any other threads from the next molecule do.
>
> In other words:
>
> - If an oxygen thread arrives at the barrier when no hydrogen threads are present, it has to wait for two hydrogen threads.
> - If a hydrogen thread arrives at the barrier when no other threads are present, it has to wait for an oxygen thread and another hydrogen thread.
>
> We don’t have to worry about matching the threads up explicitly; that is, the threads do not necessarily know which other threads they are paired up with. The key is just that threads pass the barrier in complete sets; thus, if we examine the sequence of threads that bond and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.
>
> Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.
>
>  
>
> **Example 1:**
>
> ```
> Input: "HOH"
> Output: "HHO"
> Explanation: "HOH" and "OHH" are also valid answers.
> ```
>
> **Example 2:**
>
> ```
> Input: "OOHHHH"
> Output: "HHOHHO"
> Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
> ```
>
>  
>
> **Constraints:**
>
> - Total length of input string will be 3*n*, where 1 ≤ *n* ≤ 30.
> - Total number of `H` will be 2*n* in the input string.
> - Total number of `O` will be *n* in the input string.



# 代码

```python
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
```



# 背景

Python中有多种队列实现，比如collections.deque, multiprocessing.Queue,,threading.Queue, asyncio.Queue, heapq等

在这里可以使用collections.deque或者threading.Queue。

deque文档说明：

> *class* `collections.deque`([*iterable*[, *maxlen*]])
>
> Returns a new deque object initialized left-to-right (using [`append()`](https://docs.python.org/3/library/collections.html#collections.deque.append)) with data from *iterable*. If *iterable* is not specified, the new deque is empty.
>
> Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support **thread-safe, memory efficient appends and pops from either side** of the deque with approximately the same O(1) performance in either direction.



#  说明

将releaseHydrogen函数和releaseOxygen函数本身入到各自队列，达到两个氢原子一个氧原子就出队并调用