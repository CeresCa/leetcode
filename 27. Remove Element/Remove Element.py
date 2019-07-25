class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}

    def removeElement(self, nums, val):
        # why I got error when I replaced nums[:] with nums
        nums[:] = [x for x in nums if x != val]
        return len(nums)
