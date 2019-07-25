class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        lastNonZeroIndex = 0
        for i in range(lens):
            if nums[i] != 0:
                nums[lastNonZeroIndex] = nums[i]
                lastNonZeroIndex += 1
        for j in range(lastNonZeroIndex, lens):
            nums[j] = 0
