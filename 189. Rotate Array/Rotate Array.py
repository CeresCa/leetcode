class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.

    # O(n) space
    def rotate(self, nums, k):
        temp = [i for i in nums]
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = temp[i]
