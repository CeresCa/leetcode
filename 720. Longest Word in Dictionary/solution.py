class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words)
        hashset = set([""])
        longest = ""
        for w in words:
            if len(w) == 1 or w[:-1] in hashset:
                longest = w if len(w) > len(longest) else longest
                hashset.add(w)
        return longest
