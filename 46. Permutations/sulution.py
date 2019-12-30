class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.recursive(nums, 0, len(nums), result)
        return result
    
    
    def recursive(self, nums, begin, end, result):
        if begin == end:
            result.append(nums.copy())
            return
        else:
            for i in range(begin, end):
                nums[begin], nums[i] =  nums[i], nums[begin]
                self.recursive(nums, begin+1, end, result)
                nums[begin], nums[i] =  nums[i], nums[begin]
        