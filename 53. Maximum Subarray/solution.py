class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, current = nums[0], nums[0]
        for num in nums[1:]:
            current = max(current + num, num)
            max_sum = max(current, max_sum)
        return max_sum