class Solution:
    # @param {integer} n
    # @return {boolean}
    # using set
    def isHappy(self, n):
        numSet = set()
        while n != 1 and n not in numSet:
            numSet.add(n)
            numSum = 0
            while n:
                digit = n % 10
                numSum += digit ** 2
                n /= 10
            n = numSum
        return n == 1


        # one line solution:
        # return self.isHappy(sum([int(i) ** 2 for i in str(n)])) if n > 4 else n == 1
