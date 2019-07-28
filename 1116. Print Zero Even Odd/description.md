#  题目

> Suppose you are given the following code:
>
> ```java
> class ZeroEvenOdd {
>   public ZeroEvenOdd(int n) { ... }      // constructor
>   public void zero(printNumber) { ... }  // only output 0's
>   public void even(printNumber) { ... }  // only output even numbers
>   public void odd(printNumber) { ... }   // only output odd numbers
> }
> ```
>
> The same instance of `ZeroEvenOdd` will be passed to three different threads:
>
> 1. Thread A will call `zero()` which should only output 0's.
> 2. Thread B will call `even()` which should only output even numbers.
> 3. Thread C will call `odd()` which should only output odd numbers.
>
> Each of the thread is given a `printNumber` method to output an integer. Modify the given program to output the series `010203040506`... where the length of the series must be 2*n*.
>
>  
>
> **Example 1:**
>
> ```
> Input: n = 2
> Output: "0102"
> Explanation: There are three threads being fired asynchronously. One of them calls zero(), the other calls even(), and the last one calls odd(). "0102" is the correct output.
> ```
>
> **Example 2:**
>
> ```
> Input: n = 5
> Output: "0102030405"
> ```

##  总结

交替输出0，奇/偶，直到n为止，并且长度为2n



#  代码

```python
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sem = threading.Semaphore(1)
        self.even_sem = threading.Semaphore(0)
        self.odd_sem = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(self.n):
            self.zero_sem.acquire()
            printNumber(0)
            self.even_sem.release() if i % 2 else self.odd_sem.release()

    def even(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()

    def odd(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.zero_sem.release()
```



##  说明

采用信用量实现，打印之前获得各方法对应的信号量，

打印0之后判断之后是奇数还是偶数来释放对方信号量，

打印奇/偶之后释放打印0的信号量