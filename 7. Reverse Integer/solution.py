class Solution:
    def reverse(self, x: 'int') -> 'int':
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        result = 0
        while x >= 1:
            rem = x % 10
            x = x // 10
            result = result * 10 + rem
        result *= sign
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result
