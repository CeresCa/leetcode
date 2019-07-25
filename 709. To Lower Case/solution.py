class Solution:
    def toLowerCase(self, str: str) -> str:
        lower = ""
        gap = ord("A") - ord("a")
        for s in str:
            if "A" <= s <= "Z":
                lower += chr(ord(s) - gap)
            else:
                lower += s
        return lower

