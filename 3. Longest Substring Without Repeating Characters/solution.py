class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0  # 字串起点
        max_len = 0
        used = {}  # 记录出现过的字符和下表
        length = len(s)
        # 滑动窗口
        for i in range(length):
            if s[i] in used and start <= used[s[i]]:  # 当出现之前已经访问过的字符，更新起点
                start = used[s[i]] + 1
            max_len = max(max_len, i - start + 1)  # 动态更新最大子串长度
            used[s[i]] = i

        return max(max_len, (len(s) - start))  # 最大长度和最后子串长度比较

