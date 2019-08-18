class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        for i in range(len(s)):
            if len(s) - 1 <= len(result) / 2:
                break
            temp1 = self.checkPalindrome(s, i, i)
            if len(temp1) > len(result):
                result = temp1
            temp2 = self.checkPalindrome(s, i, i + 1)
            if len(temp2) > len(result):
                result = temp2

        return result

    def checkPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
