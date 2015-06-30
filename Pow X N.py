class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        res = self.myPow(x, n / 2)
        if n % 2 == 0:
            return res * res
        else:
            return res * res * x
