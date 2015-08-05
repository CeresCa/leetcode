class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.

    def merge(self, nums1, m, nums2, n):
        k = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        # if B is longer than A just copy the rest of B to A location,
        # otherwise no need to do anything
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
