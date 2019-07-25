class Solution:
    # @param {integer[]} nums
    # @return {integer}

    # Just a trick
    # def removeDuplicates(self, nums):
    #     # Use nums[:] instead of nums 
    #     # such that the array can be modified inplace
    #     nums[:] = sorted(set(nums))
    #     return len(nums)

    def removeDuplicates(self, nums):
        if not nums:
            return 0

        cursor = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cursor]:
                cursor += 1
                nums[cursor] = nums[i]
        return cursor + 1
