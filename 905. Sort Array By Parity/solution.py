class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [n for n in A if not n % 2] + [n for n in A if n % 2]

