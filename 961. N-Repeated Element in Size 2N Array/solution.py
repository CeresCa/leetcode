class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counts = {}
        for a in A:
            if a not in counts:
                counts[a] = 1
            else:
                return a
