class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        sourceMap, targetMap = dict(), dict()
        for i in range(len(s)):
            source, target = (
                sourceMap.get(t[i]),
                targetMap.get(s[i]),
            )  # use dict().get() instead of index
            if source is None and target is None:
                sourceMap[t[i]], targetMap[s[i]] = s[i], t[i]
            elif source != s[i] or target != t[i]:
                return False
        return True

    # short version:
    # def isIsomorphic(self, s, t):
    # return len(set(zip(s, t))) == len(set(s)) == len(set(t))
