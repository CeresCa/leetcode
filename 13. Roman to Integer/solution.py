class Solution:
    def romanToInt(self, s: str) -> int:
        map_ = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = curr = prev = 0
        for i in s[::-1]:
            curr = map_[i]
            if curr < prev:
                ans -= curr
            else:
                ans += curr
            prev = curr
        return ans
