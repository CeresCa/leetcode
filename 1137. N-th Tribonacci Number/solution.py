class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0, 1, 1]
        if n <= 2:
            return res[n]
        a, b, c = 0, 1, 1
        for i in range(3, i + 1):
            a, b, c = b, c, a + b + c
        return c
