class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums is None:
            return False
        elif len(nums) != len(set(nums)):
            return True
        else:
            return False

        # this solution can be simplified like this:
        # return len(nums) > len(set(nums))
