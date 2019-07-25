class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        startPos = 0
        maxLen = 0
        usedChar = dict()

        for i in range(len(s)):
            if s[i] in usedChar and startPos <= usedChar[s[i]]:
                startPos = usedChar[s[i]] + 1
            else:
                maxLen = max(maxLen, i - startPos + 1)

            usedChar[s[i]] = i

        return max(maxLen, (len(s) - startPos))
