class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        start = 0
        ans = []
        nums.append(99999999999999999)
        for i in range(0, len(nums)):
            if nums[i] - nums[start] != i - start:
                if i - start > 1:
                    ans.append('{}->{}'.format(nums[start], nums[i - 1]))
                else:
                    ans.append('{}'.format(nums[start]))

                start = i
        return ans

# print(Solution().summaryRanges([-1, 0, 1, 2, 4, 5, 7]))
