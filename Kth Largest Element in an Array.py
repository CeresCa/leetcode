from heapq import *
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):

        heapify(nums)
        sortedNums = [heappop(nums) for i in range(len(nums))]
        return sortedNums[-k]

