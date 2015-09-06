class Solution(object):
        # Easy understand but too slow

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(2):
                tmp = self.checkPalindrome(s, i, i + j)
                if len(tmp) > len(result):
                    result = tmp
        return result

    def checkPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
