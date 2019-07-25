class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        idx = sorted(range(len(nums)), key=lambda x: nums[x])
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums) and nums[idx[j]] - nums[idx[i]] <= t:
                if abs(idx[i] - idx[j]) <= k:
                    return True
                j += 1
        return False
