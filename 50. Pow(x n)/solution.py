
# Recursive
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        res = self.myPow(x, n >> 1)
        if n & 1 == 0:
            return res * res
        else:
            return res * res * x


# Iterative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow