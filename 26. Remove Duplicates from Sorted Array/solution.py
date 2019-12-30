class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cursor = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cursor]:
                cursor += 1
                nums[cursor] = nums[i]
        return cursor + 1