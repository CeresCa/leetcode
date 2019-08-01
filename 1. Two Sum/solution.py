class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmpNum = {}  # 使用字典记录值和下表的关系，判断target和当前值的差是否在list中
        for i in range(len(nums)):
            if target - nums[i] in tmpNum:
                return (tmpNum[target - nums[i]], i)
            else:
                tmpNum[nums[i]] = i
