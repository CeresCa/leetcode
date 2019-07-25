class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dictionary = {}
        for index, value in enumerate(nums):
            if value in dictionary and index - dictionary[value] <= k:
                return True
            else:
                dictionary[value] = index
        return False
