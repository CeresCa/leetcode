class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}

    # use sorting
    # def isAnagram(self, s, t):
    #     return sorted(s) == sorted(t)

    # use array
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counts = [0 for i in range(26)]
        for i in range(0, len(s)):
            counts[ord(s[i]) - ord("a")] += 1
            counts[ord(t[i]) - ord("a")] -= 1
        for i in range(0, 26):
            if counts[i]:
                return False
        return True
