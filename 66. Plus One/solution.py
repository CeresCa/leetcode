class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        return [int(i) for i in str(num + 1)]