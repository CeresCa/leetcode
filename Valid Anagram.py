class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}

    # use sorting
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
