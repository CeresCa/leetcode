class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        #
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print (solution.hammingWeight(11))

#
#