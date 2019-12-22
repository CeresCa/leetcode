class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}  # store (num, index) pair in dict
        for i, num in enumerate(nums):
            if target - num in numIndex:
                return (numIndex[target - num], i)
            else:
                numIndex[num] = i
