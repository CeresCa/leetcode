class Solution:
    # @param {integer} n
    # @return {integer}

    def numTrees(self, n):
        count = [0 for i in range(n + 2)]
        count[0] = 1
        count[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                count[i] += count[j] * count[i - j - 1]
        return count[n]
